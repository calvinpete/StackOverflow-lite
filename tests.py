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


if __name__ == "__main__":
    unittest.main()
