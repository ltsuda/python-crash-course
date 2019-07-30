guest_list = ['Sterling', 'Reda', 'Audrey', 'Kelly', 'Thersa']
print(f'Original guest list {guest_list}')
print("Ops, the table is not big enough "
      "we need to choose only two of our guests")

popped_person = guest_list.pop()
print(f"Sorry {popped_person}, we don't have enough space to invite you")
popped_person = guest_list.pop()
print(f"Sorry {popped_person}, we don't have enough space to invite you")
popped_person = guest_list.pop()
print(f"Sorry {popped_person}, we don't have enough space to invite you")

print(f'Please, would you still like to come to the event {guest_list[0]}?')
print(f'Please, would you still like to come to the event {guest_list[-1]}?')

del guest_list[0]
del guest_list[0]

print(f"Wow, our list {guest_list} is empty now")
