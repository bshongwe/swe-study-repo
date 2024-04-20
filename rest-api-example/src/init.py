from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Import routes
from app import routes

