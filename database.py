import psycopg2


class DatabaseConnection(object):
    """This class holds all methods that create read update and delete data in the database"""

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="run", user="calvin", password="310892", host="127.0.0.1", port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Yes")
        except:
            print ("No connection to the database")

    def create_table_users(self):
        """ create user table"""
        user_table = "CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, " \
                     "password VARCHAR(50) NOT NULL);"
        self.cursor.execute(user_table)
        self.connection.commit()
        print ("users table successfully created")
        # self.connection.close()

    def create_table_questions(self):
        """create questions table"""
        question_table = "CREATE TABLE questions( question_id SERIAL PRIMARY KEY, " \
                         "question_title VARCHAR(255) NOT NULL, " \
                         "question_details VARCHAR(255) NULL);"
        self.cursor.execute(question_table)
        self.connection.commit()
        print("questions table successfully created")
        # self.connection.close()

    def create_table_answers(self):
        """create answers table"""
        answers_table = "CREATE TABLE answer_table (answer_id SERIAL PRIMARY KEY, answer VARCHAR(255) NULL, " \
                        "status VARCHAR(10) NULL," \
                        "question_id INT NOT NULL REFERENCES questions(question_id) ON DELETE CASCADE)"
        self.cursor.execute(answers_table)
        self.connection.commit()
        # self.connection.close()

    def insert_users(self, username, password):
        """create users"""
        insert_user = "INSERT INTO users(username, password) VALUES(%s, %s);"
        self.cursor.execute(insert_user, (username, password))
        self.connection.commit()
        print ("User successfully added")
        # self.connection.close()

    def insert_questions(self, question_title, question_details):
        """create questions"""
        insert_question = "INSERT INTO questions(question_title, question_details) VALUES(%s, %s);"
        self.cursor.execute(insert_question, (question_title, question_details))
        self.connection.commit()
        # self.connection.close()

    def insert_answers(self, answer, qn_id):
        """create answers"""
        insert_answers = "INSERT INTO answer_table(answer, question_id) VALUES(%s, %s);"
        self.cursor.execute(insert_answers, (answer, qn_id))
        self.connection.commit()
        # self.connection.close()

    def select_all_questions(self):
        """get all questions"""
        select_questions = "SELECT * FROM questions;"
        self.cursor.execute(select_questions)
        all_questions = self.cursor.fetchall()
        questions = {}
        for row in all_questions:
            questions[row[0]] = {"qn_title": row[1],
                                 "qn_details": row[2]
                                 }
        return questions
        # self.connection.close()

    def select_one_question(self, qn_id):
        """get one question"""
        select_question = "SELECT questions.question_title, questions.question_details, " \
                          "answer_table.answer, answer_table.status FROM questions " \
                          "INNER JOIN answer_table ON answer_table.question_id = questions.question_id " \
                          "WHERE questions.question_id = %s;"
        self.cursor.execute(select_question, [qn_id])
        a_question = self.cursor.fetchall()
        answer_list = []
        for row in a_question:
            answer_list.append({"answer": row[2], "status": row[3]})
            single_qn = {
                "qn_title": row[0],
                "qn_details": row[1],
                "answers": answer_list
            }
        return single_qn
        # self.connection.close()

    def delete_question(self, qn_id):
        """delete questions"""
        delete_question = "DELETE FROM questions WHERE question_id = %s;"
        self.cursor.execute(delete_question, [qn_id])
        self.connection.commit()
        print ("Question successfully deleted")
        # self.connection.close()

    def mark_answer(self, answer_id):
        """mark an answer as preferred"""
        update_answer = "UPDATE answer_table SET status = 'preferred' WHERE answer_id = %s"
        self.cursor.execute(update_answer, [answer_id])
        self.connection.commit()
        print ("Answer successfully marked")
        # self.connection.close()

#
# if __name__ == "__main__":
#     database = DatabaseConnection()
