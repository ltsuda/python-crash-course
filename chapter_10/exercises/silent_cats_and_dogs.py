def cats_and_dogs(filename):
    """Print tha name of the cats and dogs from some files."""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        if 'cats' in filename:
            print(f"The cats name are\n{contents}")
        elif 'dogs' in filename:
            print(f"The dogs name are\n{contents}")
        else:
            print(f"The pets name are\n{contents}")


pets = ['exercises/cats.txt', 'exercises/dogs.txt', 'exercises/snakes.txt']
for pet in pets:
    cats_and_dogs(pet)
