favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

person = ['phil', 'mike', 'sarah', 'john']

for name in person:
    if name in favorite_languages.keys():
        print(f"Thank you for participating {name.title()}!")
    else:
        print(f"Please {name.title()}, could you vote in the poll?")
