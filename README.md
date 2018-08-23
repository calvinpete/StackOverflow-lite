
[![Build Status](https://travis-ci.org/calvinpete/StackOverflow-lite.svg?branch=API)](https://travis-ci.org/calvinpete/StackOverflow-lite)              [![Coverage Status](https://coveralls.io/repos/github/calvinpete/StackOverflow-lite/badge.svg?branch=API)](https://coveralls.io/github/calvinpete/StackOverflow-lite?branch=API)                    <a href="https://codeclimate.com/github/calvinpete/StackOverflow-lite/maintainability"><img src="https://api.codeclimate.com/v1/badges/c55bf3e0bac3e3a2b0e9/maintainability" /></a>

# StackOverflow-lite API Endpoints

The api endpoints enable you to view all questions, post a question, view a single question and post an answer to a question.

## Getting Started

To run the application, make sure you have the following installed.

### Prerequisites

```
Git
Python IDE
Flask
Flask Restful
Virtual Enviroment
```

### Starting the application

Clone the project

```
https://github.com/calvinpete/StackOverflow-lite/tree/API
```

Activate the virtualenv

```
source venv/bin/activate
```

Install the packages.

```
pip install -r requirements.txt
```

Run the application

```
python run.py
```

## Running the tests

```
pytest tests.py
```

### Running tests with coverage

You run tests with coverage by running this command in the terminal

```
nosetests --with-coverage --cover-package=app
```

### Features

|               Endpoint                 |          Functionality      |
| -------------------------------------- |:---------------------------:|
| GET /questions                         | Fetch all questions         |
| GET /questions/<questionId>            | Fetch a specific question   |
| POST /questions/<questionId>/answers   | Add a question              |
| POST /questions/<questionId>/answers   | Add an answer               |


## Deployment

The app is deployed on this [link](https://stackoverflowlitev1-api.herokuapp.com/api/v1/questions)

## Built With

* [Python](https://www.python.org/) - General Purpose Language
* [Flask](http://flask.pocoo.org/) - Python Micro Web Framework

## Authors

**Calvin Tinka**

## License

This app is open source hence free to all users