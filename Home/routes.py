#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from flask import request 
from sqliteConn import Sqlite
from flask import Blueprint 
from flask import session, flash 
from flask import render_template, redirect, url_for 

# Creating the blueprint object 
home = Blueprint('home', __name__, template_folder='templates', static_folder='static'); 

# Creating an instance of the database 
db = Sqlite(); 

# Creating the home page 
@home.route("/", methods=["GET"])
def HomePage():
    # Rendering the html template file 
    return render_template('home.html'); 