#Here you will see the numnber 10 coming, in the line when its printing
# It will be said there are 10 types of people. 
x = "There are %d types of people." % 10

#Those who know binary and thoe who dont
# The s% prints it out and puts it in good order
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#String
print x
print y

#Here you will see the printing from line 9
#Those who know and thow who dont
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#Here W and E will be put togehter to print out all in one line.
print joke_evaluation % hilarious
#String
w = "This is the left side of..."
e = "a string with a right side."

print w + e

# It makes a string longer,  becouse it is typed print w + e and that means
# W + E will be printed together and make it a longer string 