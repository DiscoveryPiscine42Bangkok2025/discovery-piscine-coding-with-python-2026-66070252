import sys

if len(sys.argv) == 2:
    input_string = sys.argv[1]
        
    zs_found = "".join([char for char in input_string if char == 'z'])
        
    if zs_found:
        print(zs_found)
    else:
        print("none")
else:
    print("none")
