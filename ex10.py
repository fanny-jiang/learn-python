# Ex10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# what is the point of the double backslash??

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# while True:
#   for i in ["/","-","|","\\","|"]:
#     print "%s\r" % i,

s9 = "I contain a BACKSPACE\b"
s10 = "I contain a BACKK\bSPACE AND a \nNEWLINE and a \rLINEFEED"
s11 = "I ve got a FORM\fFEED!"

print s9
print s10
print s11