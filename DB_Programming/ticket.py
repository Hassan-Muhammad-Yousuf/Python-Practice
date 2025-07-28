import psycopg2


# Database Connection

conn = psycopg2.connect(
    database = "transport",
    user = "postgres",
    password = "1947",
    host = "localhost",
    port = "5432"
)

print ("Connection Sucessfull")

# Create Cursor
cur = conn.cursor()

# Create Table Passenger
sql_create_table = cur.execute('''CREATE TABLE IF NOT EXISTS passenger(
    ticketnumber VARCHAR(8) NOT NULL,
    startstation VARCHAR(25) NOT NULL,
    endstation VARCHAR(25) NOT NULL,
    tickettype VARCHAR(15) NOT NULL,
    price FLOAT,
    valid BOOLEAN,
    PRIMARY KEY(ticketnumber)                     
    )
''')

# Commit Query
conn.commit()

# Insert Data into Table

sql_insert_data = cur.execute("INSERT INTO passenger(ticketnumber, startstation," \
"endstation, tickettype, price, valid)" \
"VALUES('BR5134','Hackersher Market','Ostkurez'," \
"'1st Klasse', 24.25, True)")

sql_insert_data1 = cur.execute("INSERT INTO passenger VALUES('BR2164','Potsdam'," \
"'Wansee','1st Klasse', 12.25, True)")

print(cur.rowcount,'inserted')

# Commit Query
conn.commit()

# Advance rows insertion 
query = """
INSERT INTO passenger 
(ticketnumber, startstation, endstation, tickettype, price, valid)
VALUES 
(%s, %s, %s, %s, %s, %s)
"""

data = [
    ('BR1001', 'Alexanderplatz', 'Spandau', '2nd Klasse', 18.50, False),
    ('BR1002', 'Zoo', 'Friedrichstrasse', '1st Klasse', 42.00, True),
    ('BR1003', 'Ostbahnhof', 'Wannsee', '2nd Klasse', 22.75, False),
    ('BR1004', 'Potsdam', 'Charlottenburg', '1st Klasse', 39.90, True),
    ('BR1005', 'Tiergarten', 'Lichtenberg', '2nd Klasse', 15.00, False),
    ('BR1006', 'Südkreuz', 'Gesundbrunnen', '2nd Klasse', 19.00, True),
    ('BR1007', 'Tempelhof', 'Neukölln', '1st Klasse', 45.00, True),
    ('BR1008', 'Hauptbahnhof', 'Schönefeld', '2nd Klasse', 17.20, False),
    ('BR1009', 'Westkreuz', 'Marzahn', '1st Klasse', 38.50, True),
    ('BR1010', 'Ostkreuz', 'Lichterfelde', '2nd Klasse', 21.00, False),
]

#commit data at once 
cur.executemany(query, data)
conn.commit()


# Read data from database table
sql_read_data = cur.execute(" SELECT * FROM passenger")
res = cur.fetchall()


# update database Table

sql_update_table = cur.execute("""
    UPDATE passenger
    SET valid = CASE
        WHEN price > 30.00 THEN TRUE
        ELSE FALSE
    END
""")

# commit query
conn.commit()


# Delete from Database
sql_delete_table = cur.execute("DELETE FROM passenger WHERE price < 15.00")

# commit query
conn.commit()


# Add a new cloumn in the table
sql_alter_table =  cur.execute("ALTER TABLE passenger ADD COLUMN date VARCHAR(10)," \
"ADD COLUMN journeytype VARCHAR(10)")

# commit query
conn.commit()


# Read datafrom database by using indexes

# update table and set date for today
sql_update_table1 = cur.execute("UPDATE passenger SET date = '26-07-2025'")

# commit query
conn.commit()

# Update the table set date old where validation is false
sql_update_table2 = cur.execute("UPDATE passenger SET date = '26-06-2025' WHERE valid = 'FALSE'")

# commit query
conn.commit()

# Update the table set journeytype to 'single'
sql_update_table3 = cur.execute("UPDATE passenger SET journeytype = 'single'")

# Update journeytype to 'Return' where price > 35.00 
sql_update_table4 = cur.execute("UPDATE passenger SET journeytype = 'Return' WHERE price > 35.00 ")

# commit query
conn.commit()


for y in res:
    print("******************** Ticket Information ********************")
    print('Ticket Number: ',y[0])
    print('Start Station: ',y[1])
    print('End Station: ',y[2])
    print('Ticket Type: ',y[3])
    print('Price: ',y[4])
    print('Valid? ',y[5])
    print('Date: ',y[6])
    print('journeytype: ',y[7])

# Commit Query
conn.commit()


#close connection
conn.close()
