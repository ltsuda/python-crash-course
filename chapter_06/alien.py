alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just earned {new_points}!')

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 25
print(f"The alien one is {alien_1['color']}")
alien_1['color'] = 'yellow'
print(f"Now, the alien one is {alien_1['color']}")

del alien_1['points']
print(alien_1)

print('List of dictionaries')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'red', 'points': 25}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
