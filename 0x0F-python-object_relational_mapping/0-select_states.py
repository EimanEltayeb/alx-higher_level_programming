#!/usr/bin/python3
""" 0-select_states.py"""


import MySQLdb
import sys


def states_list(us, ps, dab):
    """states_list"""

    db = MySQLdb.connect(host="localhost", port=3306, 
    user=us, passwd=ps, db=dab)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        id_ = row[0]
        name = row[1]
        print(f"({id_}, '{name}')")

    db.close()
if __name__ == "__main__":

    
    us = sys.argv[1]
    ps = sys.argv[2]
    dab = sys.argv[3]

    states_list(us, ps, dab)
