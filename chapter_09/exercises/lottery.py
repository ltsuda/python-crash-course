from random import choice


possibilities = [10, 3, 'b', 99, 'c', 29,
                 'e', 81,  33, 43, 'h', 72, 5, 'i', 51]
winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
