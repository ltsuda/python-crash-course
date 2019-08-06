alien = {'color': 'green', 'speed': 'slow'}

# print(alien['points']) Would throw an error
point_value = alien.get('points', 'No point value assigned.')
print(point_value)
