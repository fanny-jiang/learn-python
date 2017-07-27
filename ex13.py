from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

# when there aren't enough arguments passed to script
# ValueError: too many values to unpack

# when there are too many arguments passed to script
# ValueError: need more than 3 values to unpack

script, name, age = argv

print "Script is called:", script
print "My name is:", name
print "I am: ", age

name = raw_input("What's your name? ")
age = raw_input("How old are you? ")

print "My name is: %r and I am %r years old." % (name, age)