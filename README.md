# Arithmetic Calculator

This is a Flask API that serves as the backend for a Vue.js application. It provides endpoints to handle user authentication, perform mathematical calculations, and manage transactions.

## Live Version 
- Base URL:http://ec2-18-219-245-237.us-east-2.compute.amazonaws.com:5000 
- Swagger: http://ec2-18-219-245-237.us-east-2.compute.amazonaws.com:5000/swagger-ui
- Postman collection: https://github.com/luis-reyes/arithmetic-calculator-api/blob/main/ArithmeticCalculatorAPI.postman_collection.json
- Server: AWS EC2
- Database: AWS RDS

## Features

- User Authentication: Register and login endpoints for user authentication.
- Secure Transactions: Endpoints to perform mathematical calculations securely by authenticating requests.
- Error Handling: Proper error handling and response messages for various scenarios.
- Database Integration: Integration with a database (PostgreSQL) for storing user information and transaction data.
- Swagger documentation: Available at: /swagger-ui

## Technologies Used

- Python: A programming language used for building the Flask API.
- Flask: A micro web framework for building APIs with Python.
- Flask-RESTful: An extension for Flask that simplifies building RESTful APIs.
- SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library.
- JWT (JSON Web Tokens): A standard for securely transmitting information between parties as a JSON object.
- Database: Integration with PostgreSQL database for data storage.

## API Endpoints

The following are the main API endpoints provided by the Flask API:

- `/api/v1/users/register`:
  - Method: POST
  - Description: Register a new user with username and password.
  - Request Body: `{ "username": "example", "password": "password123" }`

- `/api/v1/users/login`:
  - Method: POST
  - Description: Authenticate and log in a user with username and password.
  - Request Body: `{ "username": "example", "password": "password123" }`
  - Response: Returns a JSON Web Token (JWT) for authentication.

- `/api/v1/operations/`:
  - Method: GET
  - Description: Retrieve a list of available mathematical operations.
  - Authorization: Bearer Token (JWT) required in the request headers.

- `/api/v1/transactions/`:
  - Method: POST
  - Description: Perform a mathematical calculation based on the selected operation and input numbers.
  - Request Body: `{ "operation_id": 1, "num_1": 5, "num_2": 3 }`
  - Authorization: Bearer Token (JWT) required in the request headers.

## Setup and Usage

1. Clone the repository: `git clone https://github.com/your/repository.git](https://github.com/luis-reyes/arithmetic-calculator-api.git`
2. Navigate to the project directory: `cd arithmetic-calculator-api`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Set up the database:
   - Configure the database connection details in `config.py`
7. Start the Flask API: `python3 api/app.py`
8. Access the API endpoints in the Vue application: http://ec2-18-219-245-237.us-east-2.compute.amazonaws.com:5173/login .

## Configuration

The application requires the following configuration:

- Database Configuration: Update the database connection details in `config.py`
- Secret Key: Set a secret key in `config.py`

## Folder Structure

- `api`: Contains the main Flask application code.
  - `models`: Contains the database models.
  - `controllers`: Contains service modules for user authentication and calculations.
  - `utils`: Contains utility functions.
  - `tests`: Contains unit tests for the API endpoints.
  - v1
   - `resources`: Contains the API resources and endpoints.
