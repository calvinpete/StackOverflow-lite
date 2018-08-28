from flask import jsonify
from flask import make_response


errors = {
    'BadRequest': {
        "message": "Invalid entry",
        "status": 400,
                    }
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


def object_bad_request(message):
    """
    This function returns an error message for not JSON object
    :param message:
    :return:
    """
    response = make_response(jsonify({message: "Its not JSON object"}), 400)
    return response
