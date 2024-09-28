import pytest

@pytest.fixture(name='martin')
def answer_of_the_answers_forever():
    return 42


def test_answer(martin):
    assert martin==42
