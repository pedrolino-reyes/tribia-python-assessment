# Testing "The Internet" (using Python, pytest and Playwright)!

A basic Playwright and Python repo to demonstrate how we can write end to end tests for the website hosted at [http://the-internet.herokuapp.com/](http://the-internet.herokuapp.com/).

## Getting set up

1. **Install Python 3**. You'll need to have first install Python. This code was written using Python 3.13.1. .
1. **Clone this codebase**. Clone this repo to your local machine.
1. **Install Poetry**. We're using Poetry to manage all of the Python dependencies
1. **Install the dependencies**. Run `poetry install` to install all the required Python libraries.
1. **Create a local .env file**. There are some "secrets" and configuration details that we keep in a .env file. This file isn't part of the repo, to avoid putting secrets in plain text in github. Ask a friend for the login user details and then complete your .env file with the following values:

```bash
BASE_URL=http://the-internet.herokuapp.com
LOGIN_USER=<secret_login_user>
LOGIN_PASS=<secret_login_password>
```

## Running the tests

We're using pytest as our test runner. To run all the tests:

```bash
poetry run pytest
```