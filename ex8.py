# Exercise 8: Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)

# Mistakes
# => on line 8, I didn't include enough arguments for format string (3 instead of 4)

# Line 12 printed out in double quotes, because there's an apostrophe in the word, "didn't".

# %s should always be used for formatting. %r should be used for debugging information about something. %r will give the "raw programmer's" version of variable, aka the "representation".

