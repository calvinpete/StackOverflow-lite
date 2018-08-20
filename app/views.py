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

