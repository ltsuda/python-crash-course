with open('exercises/learning_python.txt') as file_object:
    lines = file_object.readlines()

contents = ''
for line in lines:
    contents += line.strip()

print(contents)
contents = contents.replace('Python', 'Swift')
print(contents)
