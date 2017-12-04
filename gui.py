import sqlite3
from sqlite3 import Error
#from tkinter import *

def init_conn(db):
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
        row = len(rows) - 1
        return rows[row]

def select_table(conn, table):
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + table + ";")
        rows = cur.fetchall()
        return rows

def main():
        database = "IoT.db"
        #window = Tk()
        #window.title("Sensorian Data")

        conn = init_conn(database)

        with conn:
                to_display = select_all(conn, "Altitude");
                print "Altitude: " + to_display[2] + " taken at time " + to_display[1]

                to_display = select_all(conn, "Pressure");
                print "Pressure: " +  to_display[2] + " taken at time " + to_display[1]

                to_display = select_all(conn, "Temperature")
                print "Temperature: "+ to_display[2] + " taken at time " + to_display[1]

                to_display = select_all(conn, "Light")
                print "Light: " + to_display[2] + " taken at time " + to_display[1]

                while True:
                        input = raw_input("Which sensor would you like to see: ")
                        to_display = select_table(conn, input)
                        print to_display

if __name__ == '__main__':
    main()
