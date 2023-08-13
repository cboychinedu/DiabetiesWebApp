#!/usr/bin/env python3 

# Importing the necessary modules 
import sqlite3 

# Specifying the path to the database file 
database_file = "customer.db" 

# Connecting to the database  
connection = sqlite3.connect(database_file) 

# Creating a cursor object 
c = connection.cursor() 

# Creating a function to show all 
def show_all():
    # Query the database  
    c.execute("SELECT rowid, * FROM customers")
    # Saving the extracted records into a variable 
    items = c.fetchall() 

    # Displaying the records in a well formated form 
    for item in items: 
        print(item) 

    # Commiting the connection 
    connection.commit() 
    


# Creating a function to add a new record to the table 
def add_one(first_name, last_name, email):
    # Executing the SQL statements 
    c.execute("INSERT INTO customers VALUES(?, ?, ?)", (first_name, last_name, email)) 

    # Commiting the connection 
    connection.commit() 


# Creating a function to add many records to the database  
def add_many(inputValues):
    # Executing the SQL statement 
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", inputValues)

    # Commiting the connection 
    connection.commit() 


# Creating a function to delete records 
def delete_one(row_id):
    # Converting the input row_id into a string 
    row_id = str(row_id) 
    # Executing the SQL statements 
    c.execute("DELETE from customers WHERE rowid = (?)", row_id) 

    # Commiting the connection 
    connection.commit()


# Creating a function to look up email 
def email_lookup(email): 
    # Executing the SQL statements 
    c.execute("SELECT rowid, * from customers WHERE email = (?) ", (email, ))
    # Creating a list to fetch the emails selected 
    items = c.fetchall()  

    # Returning the items 
    return items; 



