class Employee:
    """
    A representation of an employee information, like name and annual salary.
    """

    def __init__(self, first, last, annual_salary):
        """Store first and last name, also the annual salary."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, value=5000):
        """Increase the annual salary, by default increases 5000."""
        self.annual_salary += value
