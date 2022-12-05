#!/usr/bin/python3
""" Module for this file"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute(
        """SELECT name FROM cities
        WHERE state_id = (
            SELECT id FROM states
            WHERE name = '{}');""".format(argv[4].split()[0]))

    rows = cur.fetchall()
    if not rows:
        print()
    else:
        for row in rows:
            print(row[0])
