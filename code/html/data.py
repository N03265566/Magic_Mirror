#!/usr/bin/python
import sqlite3
import sys
import json

con = sqlite3.connect('/../log/time.db')
cur = con.cursor()

print("Content-type:text/json;charset=utf-8\n")
con.row_factory = sqlite3.Row
cur.execute("SELECT * FROM (SELECT * FROM time ORDER BY time DESC LIMIT 10) ORDER BY time ASC;")
dataset = cur.fetchall()
chartJSON = []
for row in dataset:
	chartJSON.append({"starttime": row[0], "endtime": float(row[1])})
print(json.dumps(chartJSON))
con.close()
exit(0)