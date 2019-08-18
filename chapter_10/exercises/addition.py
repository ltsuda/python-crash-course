print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quite.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You need to enter only numbers!")
    else:
        print(answer)
