#!/usr/bin/python3
'''File Doc'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''init by filename'''
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )
    cursor = database.cursor()
    rows = 'cities.id, cities.name, states.name'
    query = 'SELECT {} FROM cities JOIN states on states.id = state_id'.format(
        rows
    )
    cursor.execute(query)
    states = cursor.fetchall()
    for city in states:
        print(city)
    cursor.close()
    database.close()
