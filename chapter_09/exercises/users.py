class User:
    """Representation of a user profile"""

    def __init__(self, first_name, last_name, location, nickname):
        """Initialize user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.nickname = nickname

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


user_0 = User('john', 'doe', 'acre', 'jdoe')
user_0.description()
user_0.greet_user()
