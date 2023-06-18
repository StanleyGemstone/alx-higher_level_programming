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
    query = 'SELECT * FROM states ORDER BY id ASC'
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()
