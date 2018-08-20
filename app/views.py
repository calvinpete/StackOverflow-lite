from flask import jsonify
from flask import abort
from flask_restful import Resource
from flask import Blueprint
from flask import request
from app.data import qns_data
from app.models import QuestionsModel


api = Blueprint('api', __name__, url_prefix='/api/v1')


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
            questions.append(qns_data[question].__getattribute__("qn_title"))
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
        return jsonify({'message': 'Question added'}), 201


api.add_resource(QuestionManager, '/questions')


