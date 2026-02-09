import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
            
        low = min(start, end)
        high = max(start, end)
            
        result = list(range(low, high + 1))
            
        print(result)
            
    except ValueError:
        print("none")
else:
    print("none")
