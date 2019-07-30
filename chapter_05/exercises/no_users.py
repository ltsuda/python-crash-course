user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print(f'Hello {user}, would like to see a status report?')
        else:
            print(f'Hello {user}')
else:
    print('There is no user registered')
