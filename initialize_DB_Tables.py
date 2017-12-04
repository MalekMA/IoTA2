import sqlite3

# SQLite DB Name
DB_Name =  "IoT.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists Temperature ;
create table Temperature (
  id integer primary key autoincrement,
  Date_n_Time text,
  Temperature text
);
drop table if exists Light ;
create table Light (
  id integer primary key autoincrement,
  Date_n_Time text,
  Light text
);
drop table if exists Pressure ;
create table Pressure (
  id integer primary key autoincrement,
  Date_n_Time text,
  Pressure text
);
drop table if exists Altitude ;
create table Altitude (
  id integer primary key autoincrement,
  Date_n_Time text,
  Altitude text
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()