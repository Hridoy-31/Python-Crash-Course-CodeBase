class AnonymousSurvey:
    """ Collect anonymous answer to a survey questions """

    def __init__(self, question):
        """ Store a qiestion and prepare to store the response """
        self.question = question
        self.responses = []

    def show_question(self):
        """ to show the question of the survey """
        print(self.question)

    def store_response(self, new_response):
        """ storing the responses from the input """
        self.responses.append(new_response)

    def show_results(self):
        """ Showing the result """
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
