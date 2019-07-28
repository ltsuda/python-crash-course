squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
print(f'min = {min(squares)}')
print(f'max = {max(squares)}')
print(f'sum = {sum(squares)}')

squares = [value ** 2 for value in range(1, 11)]
print(squares)
