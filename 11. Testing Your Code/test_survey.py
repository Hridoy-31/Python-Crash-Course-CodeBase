import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class Anonymous Survey"""

    def setUp(self):
        """ set up survey and responses for further uses """
        question = "What language did you first learn to speak ?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_responses(self):
        """ Single response testing """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_triple_responses(self):
        """ Triple response testing """
        for response in self.responses:
            self.my_survey.store_response(response)
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
