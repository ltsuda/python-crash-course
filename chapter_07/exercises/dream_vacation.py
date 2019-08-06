responses = {}

poll_active = True

while poll_active:
    name = input(f"What's your name? ")
    response = input(f"If you could visit one place in the world, "
                     f"where would you go? ")
    responses[name] = response

    repeat = input(
        f"Would you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        poll_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
