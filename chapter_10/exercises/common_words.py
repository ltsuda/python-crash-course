def common_words(filename):
    """Count the approximate number of a common word in a file."""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        count_words = contents.lower().count('the ')
        print(
            f"The file {filename} has about {count_words} times the word "
            f"'the'.")


books = ['alice.txt', 'siddhartha.txt', 'little_women.txt', 'moby_dick.txt']
for book in books:
    common_words(book)
