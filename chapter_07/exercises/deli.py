sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich}')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'The {sandwich} is completed')
