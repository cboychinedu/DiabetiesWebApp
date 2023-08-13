#!/usr/bin/env python3 

# Importing the necessary modules 
import sqlite3

# Specifying the path to the database file 
databaseFile = "Database/database.db"

# Connecting to the database 
conn = sqlite3.connect(databaseFile)
 

# Creating a class for handling all the database connections 
class Sqlite: 
    def __init_(self):
        # Creating the cursor 
        self.cursor = conn.cursor()
        

    # Creating a method to show all user's 
    def showAllUsers(self): 
        self.cursor.execute("SELECT * FROM users")
        items = self.cursor.fetchall() 

        return items; 
