def count_words(filename):
    """Count the approximate number of word in a file."""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # pass // use the 'pass' statement to not report to the user the error.
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


books = ['alice.txt', 'siddhartha.txt', 'little_women.txt', 'moby_dick.txt']
for book in books:
    count_words(book)
