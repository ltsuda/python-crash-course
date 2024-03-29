places = ['paris', 'south island', 'new zealand', 'rome', 'tahiti', 'london']
print(f'Original list:\n{places}')
print(f'Sorted list:\n{sorted(places)}')
print(f'Original list is still the same:\n{places}')
print(f'Reverse sorted list:\n{sorted(places, reverse=True)}')
print(f'Original list is still the same:\n{places}')
places.reverse()
print(f'Original list is changed by reverse method:\n{places}')
places.reverse()
print(f'Original list is changed back by reverse method:\n{places}')
places.sort()
print(f'Sorting alphabetically:\n{places}')
places.sort(reverse=True)
print(f'Reverse sorting alphabetically:\n{places}')
