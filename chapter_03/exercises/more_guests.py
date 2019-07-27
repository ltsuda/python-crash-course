guest_list = ['Sterling', 'Reda', 'Audrey', 'Kelly', 'Thersa']
print(f'Original guest list {guest_list}')
guest_cannot_go = 'Sterling'
print(f"Our guest {guest_cannot_go} can't go to the event")

new_guest = 'Mike'
guest_list.remove(guest_cannot_go)
guest_list.append(new_guest)
print(f'This is the new guest list {guest_list}')

print("There's a bigger table, so we can invite more people")
guest_list.insert(0, 'Matt')
guest_list_length = len(guest_list)
middle_of_list = int(guest_list_length/2)
guest_list.insert(middle_of_list, 'Jack')
guest_list.append('John')

print(f'Please, would you like to come to the event {guest_list[0]}?')
print(f'Please, would you like to come to the event {guest_list[1]}?')
print(f'Please, would you like to come to the event {guest_list[2]}?')
print(f'Please, would you like to come to the event {guest_list[3]}?')
print(f'Please, would you like to come to the event {guest_list[4]}?')
print(f'Please, would you like to come to the event {guest_list[5]}?')
print(f'Please, would you like to come to the event {guest_list[6]}?')
print(f'Please, would you like to come to the event {guest_list[7]}?')
