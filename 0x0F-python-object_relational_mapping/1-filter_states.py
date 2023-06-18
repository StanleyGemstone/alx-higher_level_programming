#!/usr/bin/python3
'''
This script connects to a MySQL database and retrieves data from the "states" table.

Usage: python script_name.py <username> <password> <database_name>
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''
    Entry point of the script.
    '''

    # Establish a connection to the MySQL database
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    # Create a cursor object to execute SQL queries
    cursor = database.cursor()

    # Define the SQL query to select all rows from the "states" table and order them by id in ascending order
    query = 'SELECT * FROM states ORDER BY id ASC'

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Iterate over each state and print it
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    database.close()
