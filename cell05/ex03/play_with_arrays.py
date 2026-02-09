original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
new_values_set = set()
    
for value in original_array:
    if value > 5:
        new_values_set.add(value + 2)
            
new_array = list(new_values_set)
    
print(original_array)
print(new_array)
