#!/usr/bin/python3
# Task 5
""" define list_states function """
import MySQLdb
from sys import argv


def list_states():
    """
    takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa

    Args:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    # connecting to a MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # getting a Cursor in MySQL Python
    cur = db.cursor()

    # executing MySQL Queries in Python
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                AND states.name = '{:s}'\
                ORDER BY cities.id ASC".format(argv[4]))

    # obtaining & printing Query Results
    rows = cur.fetchall()
    r = [row[0] for row in rows]
    print(", ".join(r))

    # clean Up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
