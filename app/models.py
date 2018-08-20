class QuestionsModel(object):
    """The class model represents the questions.
    The __dict__ attribute holds all per-instance attributes of the object.
    """

    def __init__(self, qns):
        self.__dict__ = qns
