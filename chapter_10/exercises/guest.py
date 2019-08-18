filename = 'exercises/guest.txt'

guest_name = input('What\'s is your name? ')

with open(filename, 'w') as file_object:
    file_object.write(guest_name)

print('Your name was written to the file.')
