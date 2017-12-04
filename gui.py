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

	return rows[len(rows)]

def main():
	database = "IoT.db"
	window = Tk()
	window.title("Sensorian Data")

	conn = init_conn(database)

	with conn:
		to_display = select_all(conn, "Temperature")
		Label(window, text = "Temperature: ", bg="none", fg="black", font="none 12 bold") .grid(row=1, column = 0, sticky=W)
		Label(window, text = to_display, bg="none", fg="black", font="none 12") .grid(row=1, column = 1, sticky=W)
		
		to_display = select_all(conn, "Light")
		Label(window, text = "Light: ", bg="none", fg="black", font="none 12 bold") .grid(row=2, column = 0, sticky=W)
		Label(window, text = to_display, bg="none", fg="black", font="none 12") .grid(row=2, column = 1, sticky=W)
		
		to_display = select_all(conn, "Pressure")
		Label(window, text = "Pressure: ", bg="none", fg="black", font="none 12 bold") .grid(row=3, column = 0, sticky=W)
		Label(window, text = to_display, bg="none", fg="black", font="none 12") .grid(row=3, column = 1, sticky=W)
		
		to_display = select_all(conn, "Altitude")
		Label(window, text = "Altitude: ", bg="none", fg="black", font="none 12 bold") .grid(row=4, column = 0, sticky=W)
		Label(window, text = to_display, bg="none", fg="black", font="none 12") .grid(row=4, column = 1, sticky=W)
		

if __name__ == '__main__':
    main()
