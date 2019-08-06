current = 1
while current <= 5:
    print(current)
    current += 1


current = 0

while current < 10:
    current += 1
    if current % 2 == 0:
        continue
    print(f"The number {current} is an odd number.")
