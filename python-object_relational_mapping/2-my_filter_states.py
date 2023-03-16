#!/usr/bin/python3
# Task 2
""" define list_states function """
import MySQLdb
from sys import argv


def list_states():
    """
    takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument

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
    cur.execute("SELECT * FROM states WHERE BINARY name = '{:s}'\
                ORDER BY id ASC".format(argv[4]))

    # obtaining Query Results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # clean Up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
