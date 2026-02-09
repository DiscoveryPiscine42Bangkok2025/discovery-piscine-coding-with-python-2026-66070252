
num = int(input("Enter a starting number: "))
if num > 25:
        print("Error\n")
else:
    current = num
    while current <= 25:
        print(f"Inside the loop, my variable is {current}")
        current += 1
