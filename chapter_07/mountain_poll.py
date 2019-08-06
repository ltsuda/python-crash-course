responses = {}

active = True

while active:
    name = input(f"What's your name? ")
    response = input(f"Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input(
        f"Would you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
