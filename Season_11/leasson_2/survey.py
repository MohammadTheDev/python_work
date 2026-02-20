class AnonymousSurvey:
    """Collect anonymous answer to a survey question."""

    def __init__(self, question):
        """Store a question, and perpare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
