class User:
    """Representation of a user profile"""

    def __init__(self, first_name, last_name, location, nickname,
                 login_attempt=0):
        """Initialize user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.nickname = nickname
        self.login_attempt = login_attempt

    def description(self):
        """Describes the user"""
        print(f"The user full name is "
              f"{self.first_name.title()} {self.last_name.title()}.")
        print(
            f"The user is from {self.location.title()}.")
        print(
            f"The user nickname is {self.nickname.lower()}")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello {self.first_name.title()}!")

    def increment_number_served(self):
        """Increment the number of login attempts."""
        self.login_attempt += 1

    def reset_login_attempts(self):
        """Reset the login attempts to zero."""
        self.login_attempt = 0
