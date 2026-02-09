import sys

if len(sys.argv) > 2:
    params = sys.argv[1:]
        
    for arg in params[::-1]:
        print(arg)
else:
    print("none")
