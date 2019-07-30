current_users = ['Alexander Poole', 'Niamh Devine',
                 'Manha Mosley', 'Lamar Tomlinson', 'Keiren Tucker']

new_users = ['Muskaan James', 'Ryan Martinez',
             'alexander poole', 'lamar tomlinson', 'Nellie Gallagher']

current_users_lower = [user.lower() for user in current_users]

if new_users:
    for user in new_users:
        if user in current_users_lower:
            print(f'You need to choose a name different than {user}')
        else:
            print(f'The user {user} is available')
