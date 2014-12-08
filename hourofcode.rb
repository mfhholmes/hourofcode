#!/opt/rubies/ruby-2.1.2/bin/ruby
# ^^ this bit is to tell linux how to run this script
# - denotes a comment in ruby

# set the default name in case we don't have an argument
$name = "some random person"

# check if we have some arguments that look like "-n [name]"
if ARGV[0].to_s=="-n" && !ARGV[1].to_s.empty?
	#Yes! we do, so grab the name bit into the global variable
	$name = ARGV[1].to_s
end

#now DEFine a function - purely because we can
def printName
	# print the message to the screen
	puts ("hello "+ $name)
end

#now we need to call the function we've just defined, otherwise we won't actually do anything
printName
