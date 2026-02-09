def average(scores_dict):
    if not scores_dict:
        return 0.0
    
    scores = scores_dict.values()
    
    class_average = sum(scores) / len(scores)
    
    return class_average

class_3B = {
    "Alice": 18,
    "Bob": 15,
    "Charlie": 8,
    "David": 9
}
class_3C = {
    "Eve": 17,
    "Frank": 15,
    "Grace": 8,
    "Heidi": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")