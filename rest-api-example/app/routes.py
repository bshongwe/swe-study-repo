#!/usr/bin/python3
""" Book routes module"""
from flask import jsonify, request
from app import app

# Books array
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Route: Get collection
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route: Get-by-ID, with error handler
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

