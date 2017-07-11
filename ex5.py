# Exercise 5: More Variables And Printing

name = 'Zed A. Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Study Drills

# Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
# Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.

inches = 56.0
centimeters = inches * 2.54
print inches, "inches is", centimeters, "centimeters."

pounds = 107.0
kilograms = pounds * 0.45359
print pounds, "pounds is", kilograms, "kilograms."

# Search online for all of the Python format characters.

# Format Symbol	/ Conversion
# %c	character
# %s	string conversion via str() prior to formatting
# %i	signed decimal integer
# %d	signed decimal integer
# %u	unsigned decimal integer
# %o	octal integer
# %x	hexadecimal integer (lowercase letters)
# %X	hexadecimal integer (UPPERcase letters)
# %e	exponential notation (with lowercase 'e')
# %E	exponential notation (with UPPERcase 'E')
# %f	floating point real number
# %g	the shorter of %f and %e
# %G	the shorter of %f and %E

# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."

yolo = "YOLO"
print "Hello there %s" % yolo # Hello there YOLO
print "Hello there %r" % yolo # Hello there 'YOLO'

# %r prints a printable representation of an object. It'll be wrapped in quotes.