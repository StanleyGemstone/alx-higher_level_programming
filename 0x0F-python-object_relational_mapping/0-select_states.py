#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve MySQL username, password, and database name from command-line argument
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = database.cursor()

    # Execute the query to retrieve all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the states
    for row in rows:
        print(row[0], row[1])

    # Close the cursor and database connection
    cursor.close()
    database.close()
