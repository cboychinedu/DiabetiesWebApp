#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
import logging 
from flask import Flask, url_for, session 
from flask_cors import CORS 
from datetime import timedelta 
from dotenv import load_dotenv

# Importing the views 
from Home.routes import home
from Admin.routes import admin

# Loading the env variables 
load_dotenv()

# Creating the flask application 
app = Flask(__name__, static_folder=None, template_folder=None) 
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.getenv('SECRET_KEY')
app.permanent_session_lifetime = timedelta(days=24)

# Setting the cors application 
CORS(app)

# Logging 
# logging.basicConfig(filename="Logs/requests.log", level=logging.DEBUG, 
#                     format="%(asctime)s,%(message)s,%(filename)s", 
#                     datefmt="%m/%d/%Y %I:%M:%S %p")


# Register the views using the "app.register" function 
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")

# Running the flask application 
if __name__ == "__main__":
    app.run(port=5000, 
            host="localhost",
            debug=True
    )