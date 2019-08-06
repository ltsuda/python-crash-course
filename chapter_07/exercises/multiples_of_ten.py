number = input(
    "Please, type a number and I'll tell you if it's a multiple of 10. ")
number = int(number)

if number % 10 == 0:
    print(f"Cool, the number {number} is a multiple of 10.")
else:
    print(f"Sorry, the number {number} is not a multiple of 10.")
