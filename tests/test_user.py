from lib.user import User

def test_instance_created():
    user = User(1, 'Dave', 'dave@email.com')
    assert user.id == 1
    assert user.username == 'Dave'
    assert user.email == 'dave@email.com'

def test_if_returned_is_what_was_expected():
    user = User(1, 'Dave', 'dave@email.com')
    user2 = User(1, 'Dave', 'dave@email.com')
    assert user == user2

def test_if_return_value_is_formatted_correctly():
    user = User(1, 'Dave', 'dave@email.com')
    assert str(user) == 'User(1, Dave, dave@email.com)'