
import string
import random

def random_username():
    size = 5
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(size))


def test_signup_new_account(app):
    username = random_username()
    email = username + '@localhost'
    password = 'test'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)

