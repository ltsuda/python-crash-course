available_toppings = ['mushrooms', 'extra cheese',
                      'green pepper', 'olives', 'pineapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'green pepper']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Adding {topping}')
    else:
        print(f'Sorry, we are out of {topping} right now')

print('Finished making your pizza!')
