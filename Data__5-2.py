import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect('grundstoffer.db')

# Kør SQL-forespørgsel for at finde alle metaller i 4. periode
result = conn.execute("SELECT navn FROM grundstoffer WHERE periode = 4 AND elektronegativitet < 2")

# Udskriv resultatet
for row in result:
    print(row[0])
    
    # Opret forbindelse til databasen
conn = sqlite3.connect('grundstoffer.db')

# Kør SQL-forespørgsel for at finde alle gasser, der ikke er i 8. gruppe
result = conn.execute("SELECT navn FROM grundstoffer WHERE gruppe != 8 AND elektronegativitet < 2")

# Udskriv resultatet
for row in result:
    print(row[0])

# Luk forbindelsen til databasen
conn.close()
