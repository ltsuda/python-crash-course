user_names = ['alexander poole', 'niamh devine',
              'manha mosley', 'lamar tomlinson', 'admin', 'keiren tucker']

for user in user_names:
    if user == 'admin':
        print(f'Hello {user}, would like to see a status report?')
    else:
        print(f'Hello {user}')
