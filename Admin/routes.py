#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from flask import request
from sqliteConn import Sqlite 
from flask import Blueprint 
from flask import session, flash 
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static'); 

# Creating an instance of the database 
db = Sqlite(); 

# Creating the home page for the admin route 
@admin.route("/", methods=["GET", "POST"])
def HomePage(): 
    # Rendering the admin home page template file 
    return render_template("adminHome.html")