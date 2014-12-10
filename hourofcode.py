#!/usr/bin/python3
# ^^ this bit just tells linux how to run this script

# - denotes a comment in Python

# lets import some standard libraries to let us do things
# "sys" allows us to output to stdout - the command line outpt
# "getopt" allows us to process command lines arguments into our program
import sys, getopt

#python programs have to have a main function
def main(argv):
	#define the name variable that will store our name
    name = ""

	#try something that might go wrong
    try:
		# call the getopt library with the arguments and a specification for what the arguments should be
        opts, args = getopt.getopt(argv,"n:",["name="])
	# if it all goes pear-shaped, handle it here:
    except getopt.GetoptError:
		# by setting the name to something sensible
        name = "world"
	# now let's go through the list of arguments (there should only be 1)
    for opt,arg in opts:
		# if it's our name argument, grab the name value into the variable
        if opt in ("-n","--name"):
            name=arg
	# once we've got the name, print it out to the console.
    print("Hello", name)

# special bit of pythpon code that works out if we're being called as a script and does the right thing
if __name__ == "__main__":
    main(sys.argv[1:])
