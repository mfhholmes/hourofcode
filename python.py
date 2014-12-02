#!/usr/bin/python3

import sys, getopt

def main(argv):
    name = ""
    try:
        opts, args = getopt.getopt(argv,"n:",["name="])
    except getopt.GetoptError:
        name = "world"
    for opt,arg in opts:
        if opt in ("-n","--name"):
            name=arg
    print("Hello", name)

if __name__ == "__main__":
    main(sys.argv[1:])
