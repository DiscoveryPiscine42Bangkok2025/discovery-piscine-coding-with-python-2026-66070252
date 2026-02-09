num = int(input("Enter a number: "))

print(f"--- Multiplication Table for {num} ---")
        
for i in range(0, 10):
    result = num * i
    print(f"{num} x {i} = {result}")