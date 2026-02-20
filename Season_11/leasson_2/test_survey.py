# from survey import AnonymousSurvey


# def test_store_single_response():
#     """Test that a single response is stored properly."""

#     # 1. Arrange
#     question = "What language did you first learn to speak?"
#     my_survey = AnonymousSurvey(question)

#     # 2. Act
#     my_survey.store_response("English")

#     # 3. Assert
#     assert "English" in my_survey.responses

import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A sample survey for language learners."""
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    return my_survey


def test_store_single_response(language_survey):
    """Test that single response is stored properly."""
    # 'language_survey' is provided by the fixtrue
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses