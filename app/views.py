from flask import jsonify
from flask import abort
from flask_restful import Resource
from flask_restful import Api
from flask import Blueprint
from flask import request
from flask import make_response
from app.data import qns_data
from app.models import QuestionsModel


main_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(main_blueprint)


class QuestionManager(Resource):
    """This class holds the endpoints to:
    post a new question
    get all questions
    """

    def get(self):
        """
        This method initialises an empty list then it appends question titles
        returning a list of questions
        :return: questions
        """
        questions = []
        for question in qns_data:
            questions.append(question.__getattribute__("qn_title"))
        return jsonify(questions)

    def post(self):
        """
        This method checks if the request data isn't there or is there but a qn_title is missing
        then return an error code 400.
        Then assigns a qn_id using length of qns_data plus one while tolerating a missing qn_details field
        and an empty list of answers to create a question be appended to the qns_data list.
        :return: {'message': 'Question added'}, 201
        """
        if not request.json or 'qn_title' not in request.json:
            abort(400)
        question = QuestionsModel(
            qns={
                'qn_id': len(qns_data) + 1,
                'qn_title': request.json['qn_title'],
                'qn_details': request.json.get('qn_details', ""),
                'answers': []
            }
        )
        qns_data.append(question)
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
        single_qn = []
        for question in qns_data:
            if question.__getattribute__("qn_id") == qn_id:
                single_qn.extend((question.__getattribute__("qn_title"), question.__getattribute__("qn_details"),
                                 question.__getattribute__("answers")))
                return jsonify(single_qn)
        else:
            abort(404)


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
        for question in qns_data:
            if qn_id == question.__getattribute__("qn_id"):
                question.__dict__["answers"].append(request.json['answers'])
                return make_response(jsonify({'message': 'Answer added'}), 201)
        else:
            abort(404)


api.add_resource(AnswerManager, '/questions/<int:qn_id>/answers')
