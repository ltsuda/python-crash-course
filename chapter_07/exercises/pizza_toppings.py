prompt = f"What toppings do you want?"
prompt += f"\nType 'quit' when you're finished. "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza")
