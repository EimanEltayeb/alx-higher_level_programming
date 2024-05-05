#!/usr/bin/python3
""" 0-select_states.py"""


import MySQLdb
import sys


def states_list(u, p, d):
    """states_list"""

    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        id_ = row[0]
        name = row[1]
        print(f"({id_}, '{name}')")

    db.close()


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    states_list(u, p, d)
