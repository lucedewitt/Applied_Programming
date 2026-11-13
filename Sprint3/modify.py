import sqlite3

con = sqlite3.connect("library-catalog.db")
con.execute("ALTER TABLE catalog RENAME COLUMN genre TO genres")
con.commit()
con.close()