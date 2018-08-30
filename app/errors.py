from flask import jsonify
from flask import make_response

# Use of an error dictionary in order to return a specific message and a status code
# when certain errors are encountered during a request
errors = {
    'BadRequest': {
        "message": "Invalid entry",
        "status": 400,
    },
    'NotFound': {
        "message": "This page does not exist",
        "status": 404
    },
    'UserExists': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}


def question_not_found(message):
    """
    This function returns an error message for a request not found
    but may be available in the future
    :param message:
    :return:
    """
    response = make_response(jsonify({message: "Question does not exist"}), 404)
    return response


def answer_not_found(message):
    """
    This function returns an error message for updating an answer that is non existent
    :param : {message: "Answer doe not exist"}, 404
    :return:
    """
    response = make_response(jsonify({message: "Answer doe not exist"}), 404)
    return response


def question_bad_request(message):
    """
    This function returns an error message for an invalid question
    :param message:
    :return response:
    """
    response = make_response(jsonify({message: "Invalid question"}), 400)
    return response


def answer_bad_request(message):
    """
    This function returns an error message for an invalid answer
    :param message:
    :return response:
    """
    response = make_response(jsonify({message: "Invalid answer"}), 400)
    return response


def user_exists(message):
    """
    This function returns an error message for a user with a username that already exists
    :param message:
    :return response:
    """
    response = make_response(jsonify({message: "username is already taken"}), 409)
    return response

