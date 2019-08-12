
class Privileges():
    """A simple model of a list of user privileges."""

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """List the user privileges."""
        print(f"The user has these privileges")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")
