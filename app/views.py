from flask_restful import Resource
from flask_restful import Api
from flask import Blueprint
from flask import request
# from app.data import qns_data
from app.errors import *
# from app.models import QuestionsModel
from database import DatabaseConnection
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import jwt
import datetime

# import json
data = DatabaseConnection()


main_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(main_blueprint, errors=errors)


class NewUserManager(Resource):
    """This class holds the endpoint to post signup details
    """

    def post(self):
        """This method receives the details of one signing up
        checks if they exist already in the database.
        If they do, it responds with an error message.
        if not, they are inserted into a database"""
        username = request.json["username"]
        email_address = request.json["emailaddress"]
        hashed_password = generate_password_hash(request.json["password"])
        data.insert_users(username, email_address, hashed_password)
        return make_response(jsonify({'message': 'New User created'}), 201)


api.add_resource(NewUserManager, '/auth/signup')

#
# # class UserManager(Resource):
# #     """This class holds the endpoint to post log in details
# #     """
# #     def post(self):
# #         """This checks the username and password used to access then returns a token if they match """
# #         authorize = request.authorization
# #
# #         if authorize and authorize.password == 'password':
# #             token = jwt.encode({"username": authorize.username,
# #                                 "expiry":  datetime.datetime.utcnow() + datetime.timedelta(minutes=20)},
# #                                app.config['SECRET_KEY'])
# #             return jsonify({'token': token})
# #
# #         return make_response(jsonify({"Error": "Login Required"}), 401)
#
#
# api.add_resource(UserManager, '/auth/login')


class QuestionManager(Resource):
    """This class holds the endpoints to:
    post a new question
    get all questions
    """

    def get(self):
        """
        This method selects all questions from the database and returns them in a dictionary
        :return: questions
        """
        return jsonify(data.select_all_questions())

    def post(self):
        """
        This method receives the question title as well as its details from the request
        then inserts them into a database.
        :return: {'message': 'Question added'}, 201
        """
        # if "qn_title" not in request.json:
        #     return question_bad_request("Error")
        qn_title = request.json['qn_title']
        qn_details = request.json.get('qn_details', "")
        data.insert_questions(qn_title, qn_details)
        return make_response(jsonify({'message': 'Question posted'}), 201)


api.add_resource(QuestionManager, '/questions')


class SingleQuestionManager(Resource):
    """This class holds the endpoint to get one question"""

    def get(self, qn_id):
        """
        This method receives the id of the question and checks if it matches the qn_id key.
        Then it returns the value related to the key that matches the received id.
        Or else it returns an error code 404
        :param: qn_id
        :return: question in JSON format
        """
        return jsonify(data.select_one_question(qn_id))

    def delete(self, qn_id):
        """
        This method receives an id of the question then deletes the question from the database
        :param qn_id:
        :return: {"Message": "Question successfully deleted"}
        """
        data.delete_question(qn_id)
        return make_response(jsonify({"Message": "Question successfully deleted"}), 200)


api.add_resource(SingleQuestionManager, '/questions/<int:qn_id>')


class AnswerManager(Resource):
    """This class holds the endpoint to post an answer"""

    def post(self, qn_id):
        """
        This method receives a question id then inserts the answer into a database under that particular question id
        :return: {'message': 'Answer added'}
        """
        answer = request.json['answers']
        data.insert_answers(answer, qn_id)
        return make_response(jsonify({'message': 'Answer added'}), 201)


api.add_resource(AnswerManager, '/questions/<int:qn_id>/answers')


class AnswerUpdateManager(Resource):
    """This class holds the API endpoint to mark an answer as accepted"""

    def put(self, qn_id, answer_id):
        """
        This method receives the question id and answer id to trace the answer
        then updates the answer's status from null to accepted
        :param qn_id:
        :param answer_id:
        :return: {'message': 'Answer successfully chosen as preferred'}, 200
        """
        data.mark_answer(qn_id, answer_id)
        return make_response(jsonify({'message': 'Answer successfully chosen as preferred'}), 200)


api.add_resource(AnswerUpdateManager, '/questions/<int:qn_id>/answers/<int:answer_id>')
