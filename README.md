# Arithmetic Calculator API

This is the repository for the Arithmetic Calculator API, which provides a set of endpoints for performing arithmetic operations and managing user transactions.

## Features

- Perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
- Calculate the square root of a number.
- Generate random strings.
- User Starts with a default balance

## Technologies Used

- Python
- Flask
- SQLAlchemy (with PostgreSQL)
- Flask-JWT-Extended
- Flask-Smorest
- Docker

## Getting Started

To get started with the Arithmetic Calculator API, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/luis-reyes/arithmetic-calculator-api.git

2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt

3. Set up the environment variables:
  DATABASE_URI: The connection URI for the PostgreSQL database.
  SECRET_KEY: Secret key used for authentication.
  JWT_SECRET_KEY: Secret key used for JWT token generation.
  RANDOM_STRING_URL: URL for generating random strings.

4. Start the application:
   ```bash
   python api/app.py
   
## Improvements

While the Arithmetic Calculator API provides the core functionality for performing arithmetic operations and managing transactions, there are some areas that could be improved:

Error handling: Enhance the error handling mechanisms to provide meaningful error messages and appropriate HTTP status codes.
Validation: Implement input validation to ensure that only valid inputs are accepted for the arithmetic operations.
Unit tests: Add unit tests to cover the functionality of the API endpoints and ensure their correctness.
Documentation: Provide detailed documentation for the API endpoints, including request and response formats, authentication requirements, and example usage. I started configuring swagger, just need to finish the setting.
