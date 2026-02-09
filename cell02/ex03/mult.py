num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
        
result = num1 * num2
        
if result > 0:
    status = "positive"
elif result < 0:
    status = "negative"
else:
    status = "positive and negative"
        
print(f"{num1} x {num2} = {result}")
print(f"The result is {status}.")