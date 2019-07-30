cars = ['bmw', 'subaru', 'toyota']

print('Is cars[0] == subaru?')
print(cars[0].lower() == 'subaru')

print('Is cars[0] != bmw?')
print(cars[0].lower() != 'bmw')

print('Is fiat in cars?')
print('fiat' in cars)

print('Are fiat or mclaren in cars?')
print('fiat' in cars or 'mclaren' in cars)

print('The list contains more than 5 cars?')
print(len(cars) > 5)

print('Is cars[0] == bmw?')
print(cars[0].lower() == 'bmw')

print('The list contains less than 10 cars?')
print(len(cars) < 10)

print('Is fiat not in cars?')
print('fiat' not in cars)

print('Is the last car == toyota?')
print(cars[-1].lower() == 'toyota')

print('Are bmw and subaru in cars?')
print('bmw' in cars and 'subaru' in cars)
