import sqlite3
con = sqlite3.connect("tutorial.db") # create a connection to the database (creates database if it doesn't exist)
cur = con.cursor() # creates a cursor (cursors let you execute statements and fetch results from queries)

# creates table called movie with title, year, & score as columns if it doesn't already exist
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

# Creates a unique index (rule for the table) that prevents duplicate rows 
# (movie_row_unique is the name, ON movie(title, year, score) is what it applies to)
cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS movie_row_unique ON movie(title, year, score)");
con.commit();

# Check if the table exists and that checking for tables works
res = cur.execute("SELECT name FROM sqlite_master") # queries SQLite, asking for the names of known database objects (execute runs it and results are stored in res)
print(res.fetchone()) # retrieves the next single row from the results in res
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'") # queries for specifically an object named spam
print(res.fetchone() is None) # prints true if res is none (aka didn't fetch anything)


# OPTION 1 for inserting
# opens a transaction to insert rows
# ON CONFLICT(title, year, score) = violation on those columns of the index rule
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
        ON CONFLICT(title, year, score) DO NOTHING
""")
con.commit() # commits the change to the connection

# Checks to make sure the rows were selected
res = cur.execute("SELECT score FROM movie")
print(res.fetchall()) # fetchall returns all rows from res


# Option 2 for inserting
# Creates a list of tuples (tuples are immutible groups of data)
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
# inserts 3 rows from data, ? = placeholder to bind data to the query (while preventing duplicates)
cur.executemany("""INSERT INTO movie VALUES(?, ?, ?) 
                ON CONFLICT(title, year, score) DO NOTHING""", data)
con.commit()

# prints each row in the table (year, title) tuple ordered by year (low to high)
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)


# Experimentation: Find something
title = input("Enter a title: ")
year = int(input("Enter a year: "))
user_movie = (title, year)

# target title, year from movies where title, year = user_movie
res = cur.execute("SELECT title, year FROM movie WHERE title=? AND year=?", user_movie)
print(res.fetchone() is None)


# Experimentation: Filtering
cur.execute("""
    INSERT INTO movie VALUES
    ('Monty Python and the Holy Grail', 2001, 8.1),
    ('Awesome Movie', 1971, 8.1)
    ON CONFLICT(title, year, score) DO NOTHING
""")

# select = what it grabs, from = where to grab from, where = the conditions for grabbing it
res = cur.execute("SELECT title, year FROM movie WHERE title='Monty Python and the Holy Grail'")
print(res.fetchall())

# create new table from filter/querie?
cur.execute("CREATE TABLE IF NOT EXISTS movie2(title, year, score)")
cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS movie2_row_unique ON movie2(title, year, score)")
con.commit()

data = list(cur.execute("SELECT title, year, score FROM movie WHERE score=8.1"))

cur.executemany("""INSERT INTO movie2 VALUES(?, ?, ?) ON CONFLICT(title, year, score) DO NOTHING""", data)
con.commit()

# Is this the best option, or should I add to like, a dictionary or something? uhh no
# What's a view?
# A view is a saved query that behaves like a read-only table.
cur.execute("CREATE VIEW highly_rated_movies AS SELECT title, year, score FROM movie WHERE score >= 8") # create a view
for movie in cur.execute("SELECT * FROM highly_rated_movies"): # can query
    print(movie)
res = cur.execute("SELECT title FROM highly_rated_movies WHERE year > 2000") # can filter
print("> 2000:", res.fetchall())
cur.execute("DROP VIEW highly_rated_movies") # remove a view
con.commit()


# Experimentation: Aggregate functions
# Average
res = cur.execute("SELECT AVG(score) FROM movie")
average = res.fetchone()[0]
print(f"Average: {average:.1f}")

res = cur.execute("SELECT AVG(score) FROM movie2")
print(f"2nd Average:", res.fetchone()[0])

# Count
res = cur.execute("SELECT COUNT(*) FROM movie")
print("Count:", res.fetchone()[0]) # use [0] to not print (result,) and instead just result
res = cur.execute("SELECT COUNT(*) FROM movie2")
print("2nd Count:", res.fetchone()[0])

# min & Max
res = cur.execute("SELECT MAX(score) FROM movie")
print("Max:", res.fetchone()[0])
res = cur.execute("SELECT min(score) FROM movie2")
print("2nd Min:", res.fetchone()[0])

#SUM
res = cur.execute("SELECT SUM(score) FROM movie")
print("Sum:", res.fetchone()[0])

#GROUP_CONCAT
res = cur.execute("SELECT year, score FROM movie")
print("Concatonate:", res.fetchone())
res = cur.execute("SELECT GROUP_CONCAT(title) FROM movie2")
print("Concatonate group:", res.fetchone())


# Delete row that was added after first change on reruns
cur.execute("DELETE FROM movie2 WHERE title=? AND year=?", ("Awesome Movie", 1971))
con.commit()


# Updating
#General syntax:
#UPDATE table_name
#SET column_name = new_value
#WHERE condition;
cur.execute("UPDATE OR IGNORE movie2 SET year=? WHERE title=?", (2002, "Awesome Movie"))
con.commit()
res = cur.execute("SELECT title, year, score FROM movie2 WHERE title='Awesome Movie'")
print("Updated 2002:", res.fetchone())


# Close and reopen test
print()
con.close() # closes the connection

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
# selects title & year, ordering by score in DESC (desending) order
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone() # fetches the first one, aka the highest rated
# !r prints the value using it's representation (clear version), so it prints 'title' ('' show it's a string)
print(f"The highest scoring Monty Python movie is {title!r}, released in {year}")
new_con.close()