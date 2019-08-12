from user import User

user_0 = User('john', 'doe', 'acre', 'jdoe')
user_0.description()
user_0.greet_user()
print(f"Login attemtps {user_0.login_attempt}")
user_0.increment_number_served()
user_0.increment_number_served()
user_0.increment_number_served()
print(f"Login attemtps {user_0.login_attempt}")
user_0.reset_login_attempts()
print(f"Login now is {user_0.login_attempt}")
