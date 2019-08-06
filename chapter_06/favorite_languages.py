favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for person in favorite_languages.keys():
    if person in friends:
        language = favorite_languages[person].title()
        print(f"{person.title()}'s favorite programming",
              f"language is {language}")

print('\nSorted names:')
for person in sorted(favorite_languages.keys()):
    language = favorite_languages[person].title()
    print(f"{person.title()}'s favorite programming",
          f"language is {language}")

print('\nOnly values with duplicates:')
for language in favorite_languages.values():
    print(language.title())

print('\nOnly values without duplicates:')
for language in set(favorite_languages.values()):
    print(language.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', 'c++'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
