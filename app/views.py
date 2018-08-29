from flask_restful import Resource
from flask_restful import Api
from flask import Blueprint
from flask import request
from app.data import qns_data
from app.errors import *
# from app.models import QuestionsModel
from database import DatabaseConnection

# import json
data = DatabaseConnection()

main_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(main_blueprint, errors=errors)


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


api.add_resource(SingleQuestionManager, '/questions/<int:qn_id>')


class AnswerManager(Resource):
    """This class holds the endpoint to post an answer"""

    def post(self, qn_id):
        """
        This method checks if id of the question matches the qn_id key.
        Then it inserts the answer value into the answers list.
        Or else it returns an error code 404
        :return: {'message': 'Answer added'}, 201
        """
        # data = request.get_json()
        # answer = data["answers"]
        # if answer.isspace() or answer == "":
        #     return answer_bad_request("Error")
        # for question in qns_data:
        #     if qn_id == question.__getattribute__("qn_id"):
        #         question.__dict__["answers"].append(request.json['answers'])
        #         return make_response(jsonify({'message': 'Answer added'}), 201)
        # else:
        #     return question_not_found("Error")
        answer = request.json['answers']
        data.insert_answers(answer, qn_id)
        return make_response(jsonify({'message': 'Answer added'}), 201)


api.add_resource(AnswerManager, '/questions/<int:qn_id>/answers')
