import sys
def downcase_it(text):
    return text.lower()

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            result = downcase_it(arg)
            print(result)
    else:
        print("none")

main()