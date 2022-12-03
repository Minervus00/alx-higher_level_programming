#!/usr/bin/python3
""" Module for this file"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id".format(
            argv[4].split()[0]))

    rows = cur.fetchall()

    for row in rows:
        print(row)
