# Psycopg2 - Advanced String Composition
import psycopg2

# Create a database connection object
connection = psycopg2.connect('dbname=flaskappdb user=postgres password=Af$ha#19')

# Create a connection cursor ot execute sql commands
cursor = connection.cursor()
# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS table1;")

# (re)create the table1 table
# (note: triple quotes allow multiline text in python)
# Execute sql commands
cursor.execute('''
    CREATE TABLE table1 (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
    ); 
''')

# Commit changes to your database
connection.commit()
# Close cursor
cursor.close()
# Close connection
connection.close()