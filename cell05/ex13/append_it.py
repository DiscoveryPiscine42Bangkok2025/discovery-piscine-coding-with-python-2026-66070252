import sys

params = sys.argv[1:]
    
if not params:
    print("none")

for p in params:
    if not p.endswith("ism"):
        print(f"{p}ism")
