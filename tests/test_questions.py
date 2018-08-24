import unittest
from tests import FlaskAppTestCase
import json


class QuestionsTestCase(FlaskAppTestCase):
    """This is a class that runs unittests on methods that deal with questions
    """

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
        response = self.client.get("/api/v1/questions/100")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
