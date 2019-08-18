filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('Writing to a file using Python.\n')
    file_object.write('Writing second line to a file using Python.\n')

with open(filename, 'a') as file_object:
    file_object.write('Appending a line to a file using Python.\n')
    file_object.write('Appending more lines to a file using Python.\n')
