#!python

num = int(input("Enter a number less than 25: "))
if num > 25:
        print("Error")
else:
    current = num
    while current <= 25:
        print(f"Inside the loop, my variable is {current}")
        current += 1
