# Rest API example (just as in the blog post)

## Description

This project is a simple RESTful API for managing a collection of
books. It allows users to retrieve a list of books, as well as retrieve
individual books by their IDs.

## Features

- GET endpoint to retrieve all books
- GET endpoint to retrieve a specific book by ID

## Technologies Used

- Python: Programming language used for development
- Flask: Web framework used to build the REST API
- Docker: Containerization platform used to package the application and
its dependencies
- unittest: Framework for writing and running unit tests in Python

## Installation

1. Clone the repository
2. Navigate to the project directory:cd <code>rest_api_example</code>
3. Run the setup script to install dependencies: <code>./setup.sh</code>

## Usage

1. Start the Docker container:</br>
<code>docker build -t rest-api-example .</code></br>
<code>docker run -p 5000:5000 rest-api-example</code>


2. Access the API endpoints:

- GET all books: `http://localhost:5000/books`
- GET a specific book by ID: `http://localhost:5000/books/<book_id>`

## Testing
Unit tests are provided to ensure the correctness of the API endpoints.
To run the tests, execute the following command:</br>
<code>python -m unittest discover tests</code>

## Contributing
Contributions are welcome. If you find any issues or have suggestions
for improvement, please open an issue or submit a pull request.

