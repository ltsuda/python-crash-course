def display_messages(messages):
    """ Display a list of message. """
    print(f"Printing a list of messages.")
    for message in messages:
        print(f'{message.capitalize()}')


messages = ['Hello 1', 'Hello some text', 'Some text in a list']
display_messages(messages)
