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
    state_name = argv[4].replace('"', '')
    rows = 'cities.name'
    joinment = 'JOIN states on states.id = state_id'
    condition = 'WHERE states.name = "{}"'.format(state_name)
    query = 'SELECT {} FROM cities {} {}'.format(
        rows,
        joinment,
        condition,
    )
    cursor.execute(query)
    states = cursor.fetchall()
    print(', '.join(city[0] for city in states))
    cursor.close()
    database.close()
