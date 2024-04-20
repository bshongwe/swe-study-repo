#!/usr/bin/python3
"""Flask app test suite module"""
import unittest
import json
from src import app


class TestAPI(unittest.TestCase):
    """Test case class to test the API endpoints"""

    def setUp(self):
        """Set up a test client"""
        self.client = app.test_client()
        self.client.testing = True

    def test_get_books(self):
        """Test the /books endpoint to retrieve all books"""
        # Send a GET request to /books endpoint
        response = self.client.get('/books')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response data is a list of books
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_book(self):
        """Test the /books/<book_id> endpoint to retrieve a specific book"""
        # Send a GET request to /books/<book_id> endpoint for an existing book
        response = self.client.get('/books/1')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response data is a dictionary representing a book
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], 1)

    def test_get_nonexistent_book(self):
        """Test the /books/<book_id> endpoint for a non-existent book"""
        # Send a GET request to /books/<book_id> endpoint for a non-existent book
        response = self.client.get('/books/100')

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Assert that the response data contains an error message
        data = json.loads(response.data)
        self.assertIn('error', data)


if __name__ == '__main__':
    """Start test suite"""
    unittest.main()

