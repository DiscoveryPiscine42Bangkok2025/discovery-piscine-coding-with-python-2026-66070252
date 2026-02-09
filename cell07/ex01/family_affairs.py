def find_the_redheads(family_dict):
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "freanck": "red"
}
    
result = find_the_redheads(dupont_family)
print(result)