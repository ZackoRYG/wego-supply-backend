class User:
    def __init__(self):
        self.username = None
        self.password = None

    def get_username(self):
        return self.username

    def set_username(self, username):
        # Perform any validation here if needed
        self.username = username
        return True

    def set_password(self, password):
        # Perform any validation here if needed
        self.password = password

    def change_password(self, old_pass, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            return True
        else:
            return False