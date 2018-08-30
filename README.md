

# StackOverflow-lite API Endpoints

The api endpoints enable you to view all questions, post a question, view a single question, post an answer to a question asked, delete a question you posted and accept an answer to your posted question

## Getting Started

To run the application, make sure you have the following installed on your local machine.

### Prerequisites

```
Git
Flask
Flask Restful
Virtual Enviroment
```

### Starting the application

Clone the project by running this in the terminal

```
git clone https://github.com/calvinpete/StackOverflow-lite/tree/API
```

Activate the virtualenv by running this command in the terminal

```
source venv/bin/activate
```

Install the packages.

```
pip install -r requirements.txt
```

Run the application in the terminal

```
python run.py
```

## Running the tests

Run this command in the terminal

```
pytest tests.py
```

### Running tests with coverage

You can run tests with coverage by running this command in the terminal

```
nosetests --with-coverage --cover-package=app
```

### Features

|               Endpoint                           |          Functionality      |
| -------------------------------------------------|:---------------------------:|
| GET /questions                                   | Fetch all questions         |
| GET /questions/<questionId>                      | Fetch a specific question   |
| POST /questions/<questionId>/answers             | Add a question              |
| POST /questions/<questionId>/answers             | Add an answer               |
| DELETE /questions/<questionId>                   | Delete a question           |
| POST /auth/signup                                | Create an Account           |
| POST /auth/login                                 | Signup                      |




## Deployment

The app is deployed on this [link](https://stackoverflw-litev2.herokuapp.com/api/v1/)

## Built With

* [Python](https://www.python.org/) - General Purpose Language
* [Flask](http://flask.pocoo.org/) - Python Micro Web Framework

## Authors

**Calvin Tinka**

## License

This app is open source hence free to all users