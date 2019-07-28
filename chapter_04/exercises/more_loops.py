my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
my_foods.append('burger')
friends_foods.append('salad')

for food in my_foods:
    print(f'My food {food}')

for food in friends_foods:
    print(f'Friend food {food}')
