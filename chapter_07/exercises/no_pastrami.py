sandwich_orders = ['veggie', 'pastrami', 'grilled cheese',
                   'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print(f'Sorry, we are out of pastrami sandwiches')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


for sandwich in finished_sandwiches:
    print(f'I made a {sandwich} sandwich.')
