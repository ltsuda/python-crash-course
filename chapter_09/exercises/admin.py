from user import User
from privileges import Privileges


class Admin(User):
    """A simple model of a admin user."""

    def __init__(
            self,
            first_name,
            last_name,
            location,
            nickname,
            login_attempt=0):
        super().__init__(first_name, last_name, location, nickname,
                         login_attempt)
        self.privileges = Privileges()
