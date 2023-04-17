#!/usr/bin/python3

"""A script that lists all states fro the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELCECT * FROM states ORDER BY states.d ASC;")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
