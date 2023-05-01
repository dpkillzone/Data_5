import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect('grundstoffer.db')

# Opret en tabel med kolonnerne 'navn', 'periode', 'gruppe', 'elektronegativitet' og 'smeltepunkt'
conn.execute('CREATE TABLE grundstoffer (navn TEXT, periode INTEGER, gruppe INTEGER, elektronegativitet REAL, smeltepunkt REAL)')

# Indsæt nogle grundstoffer
conn.execute("INSERT INTO grundstoffer VALUES ('Hydrogen', 1, 1, 2.20, -259.14)")
conn.execute("INSERT INTO grundstoffer VALUES ('Helium', 1, 18, 0.00, -272.20)")
conn.execute("INSERT INTO grundstoffer VALUES ('Lithium', 2, 1, 0.98, 180.54)")
conn.execute("INSERT INTO grundstoffer VALUES ('Beryllium', 2, 2, 1.57, 1287.00)")
conn.execute("INSERT INTO grundstoffer VALUES ('Boron', 2, 13, 2.04, 2075.00)")

# Gem ændringerne i databasen
conn.commit()

# Luk forbindelsen til databasen
conn.close()
