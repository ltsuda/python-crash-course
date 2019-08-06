users = ['mike', 'john', 'josh']

current = 0
while current < len(users):
    age = input(f"How old are you, {users[current].title()}?\n")
    age = int(age)
    if age < 3:
        print(f"Cool, your ticket is free!")
    elif age < 12:
        print(f"Your ticket costs $10")
    else:
        print(f"Your ticket costs $15")
    current += 1
