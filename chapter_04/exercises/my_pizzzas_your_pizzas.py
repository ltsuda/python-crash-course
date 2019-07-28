pizzas = ['Pepperoni', 'Mushrooms', 'Onions', 'Sausage', 'Bacon']
for pizza in pizzas:
    print(f'I like {pizza} pizza')

print('Most types of pizza are really good!')

friend_pizzas = pizzas[:]
pizzas.append('chicken')
friend_pizzas.append('pepper rock')
print(f'My pizzas: {pizzas}')
print(f'Friend pizzas: {friend_pizzas}')
