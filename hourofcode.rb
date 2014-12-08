#!/opt/rubies/ruby-2.1.2/bin/ruby
unless ARGV[0].to_s.empty?
	$name = ARGV[0]
else
	$name = "some random person"
end
def main
	puts ("hello "+ $name)
end
main
