#!/usr/bin/python3
"""Flask application module"""
from src import app

# Entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

