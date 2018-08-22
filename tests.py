import unittest
from flask import app
from app import create_app
from app.models import QuestionsModel
import json


class FlaskAppTestCase(unittest.TestCase):
    """This class holds a setup method
    that creates the environment to run the tests as well as unittests
    """

    def setUp(self):
        """This method runs before each task by:
        creating an app
        a flask test client object
        sample data
        """
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        self.qns_data = QuestionsModel(
            qns={
                "qn_id": 1,
                "qn_title": "TypeError:<Response 36 bytes [200 OK]> is not JSON serializable",
                "qn_details": """from flask import jsonify.
                from flask_restful import Resource
                class Recipe(Resource):
                def get(self):
                return jsonify({"status": "ok", "data": ""}), 200""",
                "answers": ["""return make_response(jsonify({"status": "ok", "data": ""}), 201)"""]
            }
        )

    def test_existence(self):
        """This tests existence of an app"""
        self.assertFalse(app is None)

    def test_creation(self):
        """This tests instance of a class"""
        self.assertIsInstance(self.qns_data, QuestionsModel)

    def test_all_questions(self):
        """This tests a get method for get all questions and a response status code is 200"""
        response = self.client.get("/api/v1/questions", content_type="application/json",
                                   data=json.dumps(self.qns_data.__getattribute__("qn_title")))
        self.assertEqual(response.status_code, 200)

    def test_question_post(self):
        """This tests a method for post a question and response status code is 201 as well as the response message"""
        q_data = {"qn_title": "What is JSON?", "qn_details": ""}
        response = self.client.post("/api/v1/questions", content_type="application/json",
                                    data=json.dumps(q_data))
        self.assertEqual(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertIn("Question posted", response_message['message'])

    def test_invalid_question(self):
        """This tests for an invalid posted question"""
        q_data = {"qn_details": ""}
        response = self.client.post("/api/v1/questions", content_type="application/json",
                                    data=json.dumps(q_data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_content_type(self):
        """This tests for an invalid content type of the posted question"""
        q_data = {"qn_title": "What is blueprint in flask", "qn_details": ""}
        response = self.client.post("/api/v1/questions", content_type="application/javascript",
                                    data=json.dumps(q_data))
        self.assertEqual(response.status_code, 400)

    def test_single_question(self):
        """This tests the get method for get a single question"""
        response = self.client.get("/api/v1/questions/1", content_type="application/json",
                                   data=json.dumps(self.qns_data.__getattribute__("qn_title"),
                                                   self.qns_data.__getattribute__("qn_details"),
                                                   self.qns_data.__getattribute__("answers")))
        self.assertEqual(response.status_code, 200)

    def test_invalid_question_id(self):
        """This tests for an invalid question id used to get a question"""
        response = self.client.get("/api/v1/questions/100", content_type="application/json",
                                   data=json.dumps(self.qns_data.__getattribute__("qn_title"),
                                                   self.qns_data.__getattribute__("qn_details"),
                                                   self.qns_data.__getattribute__("answers")))
        self.assertEqual(response.status_code, 404)

    def test_post_answer(self):
        """This tests the method for post an answer and the status code is 201 as well as the response message"""
        q_data = {"answers": ["use make_response method"]}
        response = self.client.post("/api/v1/questions/1/answers", content_type="application/json",
                                    data=json.dumps(q_data))
        self.assertEqual(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertEqual("Answer added", response_message['message'])

    def test_invalid_id_for_answer_post(self):
        """This tests for an invalid question id used to post an answer"""
        q_data = {"answers": ["use make_response method"]}
        response = self.client.post("/api/v1/questions/57/answers", content_type="application/json",
                                    data=json.dumps(q_data))
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
