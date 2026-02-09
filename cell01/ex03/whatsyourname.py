def whatyourname():
    first_name = input("Hey, What is your first name? : ")
    last_name = input("And your last name? : ")
    whole_name = "Well, pleased to meet you, " + first_name + " " + last_name + "."
    return whole_name

print(whatyourname())