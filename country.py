import sqlite3

DATABASE = "top_50_populous_countries.db"

print("Welcome to the 50 Most Populous Countries DB!")
ordering = input("Order by (name, population, area, gdp): ")
ordering = ordering.lower()

#Check if the input is valid
while ordering not in ["name", "population", "area", "gdp"]:
    print("Invalid input. Please enter one of the following: name, population, area, gdp.")
    ordering = input("Order by (name, population, area, gdp): ")
    ordering = ordering.lower()

db = sqlite3.connect(DATABASE)
cursor = db.cursor()

#Get the results according to the input
if ordering == "name":
    query = "SELECT * FROM countries ORDER BY name;"
elif ordering == "population":
    query = "SELECT * FROM countries ORDER BY population;"
elif ordering == "area":
    query = "SELECT * FROM countries ORDER BY land_area_km2;"
elif ordering == "gdp":
    query = "SELECT * FROM countries ORDER BY gdp;"

cursor.execute(query)
results = cursor.fetchall()

#Print the results
for row in results:
    print(row)

db.close()
