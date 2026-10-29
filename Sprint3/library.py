import sqlite3
def main():
    # creates a database and connection
    con = sqlite3.connect("library-catalog.db")
    cur = con.cursor()

    # creates table if it doesn't already exist
    cur.execute("CREATE TABLE IF NOT EXISTS catalog(name, author, description, genre, year, length, rating)")

    # Creates a unique index (rule for the table) that prevents duplicate rows 
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS catalog_row_unique ON catalog(name, author, description, genre, year, length, rating)")
    con.commit()


    # list of starting book data
    data = [
        ("Ender's Game", "Orson Scott Card", "In order to develop a secure defense against a hostile alien race's next attack, government agencies breed child geniuses and train them as soldiers. A brilliant young boy, Andrew "Ender" Wiggin lives with his kind but distant parents, his sadistic brother Peter, and the person he loves more than anyone else, his sister Valentine. Peter and Valentine were candidates for the soldier-training program but didn't make the cut―young Ender is the Wiggin drafted to the orbiting Battle School for rigorous military training. Ender's skills make him a leader in school and respected in the Battle Room, where children play at mock battles in zero gravity. Yet growing up in an artificial community of young soldiers Ender suffers greatly from isolation, rivalry from his peers, pressure from the adult teachers, and an unsettling fear of the alien invaders. His psychological battles include loneliness, fear that he is becoming like the cruel brother he remembers, and fanning the flames of devotion to his beloved sister. Is Ender the general Earth needs? But Ender is not the only result of the genetic experiments. The war with the Buggers has been raging for a hundred years, and the quest for the perfect general has been underway for almost as long. Ender's two older siblings are every bit as unusual as he is, but in very different ways. Between the three of them lie the abilities to remake a world. If, that is, the world survives.", "Science Fiction|Fantasy|Fiction|Young Adult|Dystopia", 1985, 324, 4.31),
    ]

    # checks if there's data in catalog
    res = cur.execute("SELECT * FROM catalog")
    if (res.fetchall() == []):
        # if the table is empty, add starting data
        cur.executemany("""INSERT INTO catalog VALUES(?, ?, ?, ?, ?, ?)
                        ON CONFLICT(name, author, description, genre, year, length) DO NOTHING""", data)
        con.commit()

if __name__ == "__main__":
    main()

# genres = stored.split("|")