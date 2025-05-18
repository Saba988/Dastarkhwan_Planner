from database import get_user, add_user

def login_user(username):
    user = get_user(username)
    if user:
        return user
    else:
        return None

def register_user(username, role):
    user = get_user(username)
    if not user:
        add_user(username, role)
        return True
    return False
from database import get_user, add_user

def login_user(username):
    user = get_user(username)
    if user:
        return user
    else:
        return None

def register_user(username, role):
    user = get_user(username)
    if not user:
        add_user(username, role)
        return True
    return False


