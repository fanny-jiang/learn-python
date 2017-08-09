# Functions and Files

from sys import argv

# script and input file are being defined as arguments
script, input_file = argv

# a function called, print_all is defined, takes a file, f, and prints the output from .read() called on the file, f
def print_all(f):
  print f.read()

# a function called, rewind is defined, takes a file, f, and prints calls .seek(0) on the file. Looks like it's seeking line 0 in the file.
def rewind(f):
  f.seek(0)

# a function called, print_a_line is defined, takes a line count, and the file
# prints the line count and the output of f.readline()
def print_a_line(line_count, f):
  print line_count, f.readline()

# defines a variable, current_file, sets its value to the result of the open command called with the input file
current_file = open(input_file)

# print string
print "First let's print the whole file: \n"

# calls print_all on current file => prints all lines
print_all(current_file)

# print string
print "Now let's rewind, kind of like a tape."

# calls rewind on the current file
rewind(current_file)

# print string
print "Let's print three lines:"

# defines variable, current_line, sets its value to 1
# calls print_a_line with the current_line and current_file
current_line = 1
print_a_line(current_line, current_file)

# current_line gets incremented by one
# print_a_line is called with the new current_line and current file
current_line = current_line + 1
print_a_line(current_line, current_file)

# current_line gets incremented by one again
# print_a_line is called with the new current_line and current file
current_line = current_line + 1
print_a_line(current_line, current_file)