import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# ============================

def test_question_with_multiple_choices():
    q = Question(title="Capital of France?")
    q.add_choice("Paris", True)
    q.add_choice("London", False)
    q.add_choice("Berlin", False)
    assert len(q.choices) == 3
    assert any(c.is_correct for c in q.choices)
    assert sum(c.is_correct for c in q.choices) == 1

def test_question_points_default():
    q = Question(title="Test points default")
    assert q.points == 1

def test_question_with_negative_points():
    with pytest.raises(Exception):
        Question(title="Invalid points", points=-10)

def test_choice_text_cannot_be_empty():
    q = Question(title="Empty choice test")
    with pytest.raises(Exception):
        q.add_choice("", False)

def test_choice_text_cannot_be_too_long():
    q = Question(title="Too long choice test")
    with pytest.raises(Exception):
        q.add_choice("a" * 500, False)

def test_question_without_choices():
    q = Question(title="No choices yet")
    assert q.choices == []

def test_question_with_multiple_correct_choices():
    q = Question(title="Multiple correct answers")
    q.add_choice("Answer1", True)
    q.add_choice("Answer2", True)
    assert sum(c.is_correct for c in q.choices) == 2

def test_choices_are_linked_to_question():
    q = Question(title="Link test")
    q.add_choice("Option", True)
    assert q.choices[0] in q.choices

def test_different_questions_have_independent_choices():
    q1 = Question(title="Q1")
    q2 = Question(title="Q2")
    q1.add_choice("Yes", True)
    q2.add_choice("No", False)
    assert len(q1.choices) == 1
    assert len(q2.choices) == 1
    assert q1.choices[0].text == "Yes"
    assert q2.choices[0].text == "No"

def test_question_title_is_stored_correctly():
    q = Question(title="Custom title")
    assert q.title == "Custom title"

# ============================

@pytest.fixture
def sample_question():
    q = Question(title="2 + 2 = ?")
    q.add_choice("3", False)
    q.add_choice("4", True)
    q.add_choice("5", False)
    return q

def test_fixture_question_has_correct_choice(sample_question):
    assert any(c.is_correct for c in sample_question.choices)

def test_fixture_question_choices_count(sample_question):
    assert len(sample_question.choices) == 3