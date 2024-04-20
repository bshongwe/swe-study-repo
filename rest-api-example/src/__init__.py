#!/usr/bin/python3
""" Initialize application & import routes"""
from flask import Flask


# Initialize Flask application
app = Flask(__name__)

# Import routes
from src import routes

