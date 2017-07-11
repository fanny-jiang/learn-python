# Exercise 6: Strings and Text

# This string replaces "%d" with the decimal, 10.
x = "There are %d types of people." % 10

# binary is assigned the string, "binary"
binary = "binary"

# do_not is assigned the string, "don't"
do_not = "don't"

# y is assigned a string that replaces two %s with the string variables, binary and do_not
# string w/in a string
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x evaluated
print x

# prints y evaluated
print y

# prints string evaluated with representation of y
# string w/in a string
print "I said: %r." % x

# prints string evaluated with string, y
# string w/in a string
print "I also said: '%s'." % y

# assigns variable, hilarious to boolean, False
hilarious = False

# assigns variable, joke_evaluation to a string that evaluates %r
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation evaluated with the variable hilarious
print joke_evaluation % hilarious

# assigns w to a string
w = "this is the left side of..."

# assigns e to a string
e = "a string with a right side."

# prints the concatenation of w and e
print w + e

# Study Drills

# Go through this program and write a comment above each line explaining it.
# Find all the places where a string is put inside a string. There are four places.
# Are you sure there are only four places? How do you know? Maybe I like lying.
# there are 3 places...
# Explain why adding the two strings w and e with + makes a longer string.

