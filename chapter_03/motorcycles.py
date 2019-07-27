# Modifying original list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'original list: {motorcycles}')
motorcycles[0] = 'ducati'
print(f'modified list: {motorcycles}')
motorcycles.append('honda')
print(f'appended item to list: {motorcycles}')

# Appending items to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f'created from empty list: {motorcycles}')

# Inserting item into the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'bmw')
print(f'inserted item to: {motorcycles}')

# Deleting an item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Poping an item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an item from list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
