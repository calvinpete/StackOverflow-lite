import unittest
from tests import FlaskAppTestCase
import json


class AnswersTestCase(FlaskAppTestCase):
    """This is a class that runs unittests on post method of answers
    """

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
