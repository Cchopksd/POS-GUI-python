import sqlite3

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('db/nuuaor_db.db')
    cursor = conn.cursor()
    return conn,cursor