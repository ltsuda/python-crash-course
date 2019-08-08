def send_messages(messages, messages_sent):
    """ Display a list of message. """
    print(f"Printing a list of messages.")
    while messages:
        current = messages.pop()
        print(f'{current.capitalize()}')
        sent_messages.append(current.capitalize())


def messages_sent(messages):
    """Show a list of sent messages"""
    print(f"------- Messages sent -------")
    for message in messages:
        print(f"{message}")


messages = ['Hello 1', 'Hello some text', 'Some text in a list']
sent_messages = []
send_messages(messages, messages_sent)
messages_sent(sent_messages)
