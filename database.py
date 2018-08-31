import psycopg2
from app.errors import *


class DatabaseConnection:
    """This class holds all methods that create read update and delete records in the database"""

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="run", user="calvin", password="310892", host="127.0.0.1", port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Successfully connected to the database")
        except:
            print ("No connection to the database")

    def create_table_users(self):
        """
        This creates a user table with;
        - user id column
        - username column
        - email address column
        - password column
        """
        user_table = "CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(255) UNIQUE NOT NULL, " \
                     "email_address VARCHAR(255) UNIQUE NOT NULL, " \
                     "password VARCHAR(255) NOT NULL);"
        self.cursor.execute(user_table)
        self.connection.commit()

    def create_table_questions(self):
        """
        This creates a question table with;
        - question id column
        - question title column
        - question details column
        """
        question_table = "CREATE TABLE questions( question_id SERIAL PRIMARY KEY, " \
                         "question_title VARCHAR(255) NOT NULL, " \
                         "question_details VARCHAR(255) NULL);"
        self.cursor.execute(question_table)
        self.connection.commit()

    def create_table_answers(self):
        """
        This creates an answer table with;
        - answer_id column
        - answer column
        - status column
        """
        answers_table = "CREATE TABLE answer_table (answer_id SERIAL PRIMARY KEY, answer VARCHAR(255) NULL, " \
                        "status VARCHAR(10) NULL," \
                        "question_id INT NOT NULL REFERENCES questions(question_id) ON DELETE CASCADE)"
        self.cursor.execute(answers_table)
        self.connection.commit()

    def insert_users(self, username, email_address, password):
        """
        This method receives the username, password and email address to insert in the database.
        It checks if the the user's username or email address exist in the database.
        If it does it, returns a custom error message with a 409 status code
        """
        select_username = "SELECT * FROM users WHERE username = %s;"
        self.cursor.execute(select_username, (username,))
        user_check = self.cursor.fetchone()
        if user_check:
            return user_exists("Error")

        select_email = "SELECT * FROM users WHERE email_address = %s;"
        self.cursor.execute(select_email, (email_address,))
        email_check = self.cursor.fetchone()
        if email_check:
            return user_exists("Error")

        insert_user = "INSERT INTO users(username, email_address, password) VALUES(%s, %s, %s);"
        self.cursor.execute(insert_user, (username, email_address, password))
        self.connection.commit()
        return make_response(jsonify({'message': 'New User created'}), 201)

    def insert_questions(self, question_title, question_details):
        """This method receives the question_title and question details
        through the post a question route in the QuestionManager resource and
         inserts them into the questions table"""
        insert_question = "INSERT INTO questions(question_title, question_details) VALUES(%s, %s);"
        self.cursor.execute(insert_question, (question_title, question_details))
        self.connection.commit()

    def insert_answers(self, answer, qn_id):
        """This method receives the question id through
        the post answer route of the AnswerManager resource.
        It checks if the received question id exists in the database.
        If it does, it inserts the answer then returns a custom message with a 200 status code.
        Or else it returns a custom error message with a 404 status code"""
        check_question = "SELECT * FROM questions WHERE question_id = %s;"
        self.cursor.execute(check_question, [qn_id])
        row = self.cursor.fetchall()
        if row:
            insert_answers = "INSERT INTO answer_table(answer, question_id) VALUES(%s, %s);"
            self.cursor.execute(insert_answers, (answer, qn_id))
            self.connection.commit()
            return make_response(jsonify({'message': 'Answer added'}), 201)
        else:
            return question_not_found("Error")

    def select_current_user(self, user):
        """This method receives the decoded token then
        matches its first entry in the tuple with the username to trace the logged in user"""
        select_username = "SELECT * FROM users WHERE username = %s;"
        self.cursor.execute(select_username, (user,))
        user_check = self.cursor.fetchone()
        if user_check:
            return current_user

    def select_all_questions(self):
        """This method selects all the rows in the questions table and then
        returns a nested dictionary of questions with the question id as the key."""
        select_questions = "SELECT * FROM questions;"
        self.cursor.execute(select_questions)
        all_questions = self.cursor.fetchall()
        questions = {}
        for row in all_questions:
            questions[row[0]] = {"qn_title": row[1],
                                 "qn_details": row[2]
                                 }
        return questions

    def select_one_question(self, qn_id):
        """This method receives the question id through
        the get a question route of the SingleQuestionManager resource.
        It checks if the received question id exists in the database.
        If it does, it creates an empty list to accommodate the answers with the received qn_id,
        then it creates a single_qn dictionary to accommodate the question_title,
        question_details and a list of answers
        returning a json format custom error message with a 200 status code.
        Or else it returns a custom error message with a 404 status code"""
        select_question = "SELECT questions.question_title, questions.question_details, " \
                          "answer_table.answer, answer_table.status FROM questions " \
                          "INNER JOIN answer_table ON answer_table.question_id = questions.question_id " \
                          "WHERE questions.question_id = %s;"
        self.cursor.execute(select_question, [qn_id])
        a_question = self.cursor.fetchall()
        if a_question:
            answer_list = []
            single_qn = {}
            for row in a_question:
                answer_list.append({"answer": row[2], "status": row[3]})
                single_qn = {
                    "qn_title": row[0],
                    "qn_details": row[1],
                    "answers": answer_list
                }
            return jsonify(single_qn)
        else:
            return question_not_found("Error")

    def delete_question(self, qn_id):
        """This method receives the question id through
        the delete route of the SingleQuestionManager resource.
        It then checks if the received question id exists in the database.
        If it does, it deletes the question and answers with the exact question id
        returning a json format custom error message with a 200 status code.
        Or else it returns a custom error message with a 404 status code.
        """
        check_question = "SELECT FROM questions WHERE question_id = %s;"
        self.cursor.execute(check_question, [qn_id])
        row = self.cursor.fetchall()
        if row:
            delete_question = "DELETE FROM questions WHERE question_id = %s;"
            self.cursor.execute(delete_question, [qn_id])
            self.connection.commit()
            return make_response(jsonify({"Message": "Question successfully deleted"}), 200)
        else:
            return question_not_found("Error")

    def mark_answer(self, qn_id, answer_id):
        """
        This method receives the question id and answer id to trace the answer.
        It checks if either the question id or answer id exist in the database.
        if they do, it updates the answer's status from null to accepted
        and returns a custom message with a 200 status code
        Or else it returns a custom error message with a 404 status code.
        :param qn_id:
        :param answer_id:
        :return: {'message': 'Answer successfully chosen as preferred'}, 200
        """
        check_answer = "SELECT FROM answer_table WHERE question_id = %s AND answer_id = %s;"
        self.cursor.execute(check_answer, [qn_id, answer_id])
        row = self.cursor.fetchall()
        if row:
            update_answer = "UPDATE answer_table SET status = 'ACCEPTED' WHERE question_id = %s AND answer_id = %s;"
            self.cursor.execute(update_answer, [qn_id, answer_id])
            self.connection.commit()
            return make_response(jsonify({'message': 'Answer successfully chosen as preferred'}), 200)
        else:
            return answer_not_found("Error")


if __name__ == "__main__":
    database = DatabaseConnection()
    database.create_table_users()
    database.create_table_questions()
    database.create_table_answers()
