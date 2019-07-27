guest_list = ['Sterling', 'Reda', 'Audrey', 'Kelly', 'Thersa']
print(f'Original guest list {guest_list}')
guest_cannot_go = 'Sterling'
print(f"Our guest {guest_cannot_go} can't go to the event")

new_guest = 'Mike'
guest_list.remove(guest_cannot_go)
guest_list.append(new_guest)
print(f'This is the new guest list {guest_list}')
