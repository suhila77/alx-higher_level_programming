#!/user/bin/python3
*** Your Comments Here ***
import MySQLdb
import sys

if __name___ ** "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.CUISOR()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        paint(row)
    c.close()
    db.close()
