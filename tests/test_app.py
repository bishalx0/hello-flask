from app import welcome


def test_welcome():
    assert welcome() == "Welcome to the flask app!"

