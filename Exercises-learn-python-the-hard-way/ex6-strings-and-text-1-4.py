# create a string variable consisting of some text plus a formatted value
x = "There are %d types of people." % 10
# create a string
binary = "binary"
# create another string
do_not = "don't"
# create a third string, which includes the previous 2 strings using formatted values
y = "Those who know %s and those who %s." % (binary, do_not)  # puts a string into a string

# display the 2 complex strings by printing the variables
print x
print y

# now use those complex strings with formating in new strings
print "I said: %r." % x
print "I also said: '%s'." % y

# create a binary variable, and also a string that will include a value if one is passed in
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# display the string including a value that is passed in to be formatted into the string
print joke_evaluation % hilarious  # puts a string into a string
# addition by Selby - display the string without passing in a value to be formatted into the string
print joke_evaluation

# create 2 string variables
w = "This is the left side of..."
e = "a string with a right side."

# and show what happens when you 'add' 2 strings together. This is really a concatenation
print w + e # puts a string into a string