#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    needed = 8 - len(text)
    result = text + ("Z" * needed)
    print(result)


arguments = sys.argv[1:]
    
if not arguments:
    print("none")

for arg in arguments:
    clean_arg = arg.strip("'\"")
    if len(clean_arg) > 8:
        shrink(clean_arg)
    elif len(clean_arg) < 8:
        enlarge(clean_arg)
    else:
        print(clean_arg)
