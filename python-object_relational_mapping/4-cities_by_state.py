#!/usr/bin/python3
# Task 4
""" define list_states function """
import MySQLdb
import sys


def list_states():
    """
    lists all cities from the database hbtn_0e_4_usa

    Args:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    # connecting to a MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # getting a Cursor in MySQL Python
    cur = db.cursor()

    # executing MySQL Queries in Python
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id")

    # obtaining Query Results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean Up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
