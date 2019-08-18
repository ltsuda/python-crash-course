filename = 'exercises/guest_book.txt'


with open(filename, 'a') as file_object:
    while True:
        guest_name = input(f"What's is your name?\n"
                           f"(type 'quit' to end the program):\n")
        if guest_name == 'quit':
            break
        else:
            file_object.write(f"{guest_name}\n")
            print('Cool, your name is on the guest list now.')
