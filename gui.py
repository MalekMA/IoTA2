import sqlite3
from sqlite3 import Error
from tkinter import *

def init_conn(db)
	try:
		conn = sqlite3.connect(db)
		return conn
	except Error as e:
		print(e)

	return None

def select_all(conn, table):
	cur = conn.cursor()
	cur.execute("SELECT * FROM " + table + ";")
	rows = cur.fetchall()

	return rows(0)

def main():
	database = "IoT.db"

	conn = init_conn(database)

	with conn:
		


if __name__ == '__main__':
    main()