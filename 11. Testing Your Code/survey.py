class AnonymousSurvey:
    """ Collect anonymous answer to a survey questions """

    def __init__(self, question):
        """ Store a qiestion and prepare to store the response """
        self.question = question
        self.response = []
             
    def show_question(self):
        """ to show the question of the survey """
        print(self.question)


    