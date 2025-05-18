class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Donor(User):
    def __init__(self, username):
        super().__init__(username, "Donor")

class Volunteer(User):
    def __init__(self, username):
        super().__init__(username, "Volunteer")

class NGO(User):
    def __init__(self, username):
        super().__init__(username, "NGO")
