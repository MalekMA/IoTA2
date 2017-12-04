
import json
import sqlite3
import datetime

# SQLite DB Name
DB_Name =  "IoT.db"

#===============================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

def Temp_Data_Handler(data):

	time = str(datetime.datetime.now())

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Temperature (Date_n_Time, Temperature) values (?,?)",[time, data])
	del dbObj
	print "Inserted Temperature Data into Database."
	print ""

def Light_Data_Handler(data):

	time = str(datetime.datetime.now())

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Light (Date_n_Time, Light) values (?,?)",[time, data])
	del dbObj
	print "Inserted Light Data into Database."
	print ""

def Press_Data_Handler(data):

	time = str(datetime.datetime.now())

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Pressure (Date_n_Time, Pressure) values (?,?)",[time, data])
	del dbObj
	print "Inserted Press Data into Database."
	print ""

def Alt_Data_Handler(data):

	time = str(datetime.datetime.now())

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Altitude (Date_n_Time, Altitude) values (?,?)",[time, data])
	del dbObj
	print "Inserted Alt Data into Database."
	print ""
#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, data):
	if Topic == "IoT/Temperature":
		Temp_Data_Handler(data)
	elif Topic == "IoT/Light":
		Light_Data_Handler(data)
	elif Topic == "IoT/Pressure":
		Press_Data_Handler(data)
	elif Topic == "IoT/Altitude":
		Alt_Data_Handler(data)	

#===============================================================