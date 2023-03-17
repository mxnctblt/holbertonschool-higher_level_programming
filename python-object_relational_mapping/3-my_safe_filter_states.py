#!/usr/bin/python3
# Task 3
""" define list_states function """
import MySQLdb
from sys import argv


def list_states():
    """
    takes in arguments and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument. But this time,
    one that is safe from MySQL injections!

    Args:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    if len(argv[4]) <= 15:
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

    else:
        return


if __name__ == "__main__":
    list_states()
