with open('exercises/learning_python.txt') as file_object:
    content = file_object.read()

print(content)


with open('exercises/learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('exercises/learning_python.txt') as file_object:
    lines = file_object.readlines()

py_string = ''
for line in lines:
    py_string += line.strip()

print(py_string)
print(len(py_string))
