
from sys import argv

script, filename = argv

txt = open(filename)
# Here it printed out the text file i have saved
print "Here's your file %r:" % filename
print txt.read()

#Here you wil type the name of the text file like ex15_sample.txt
print "Type the filename again:"
file_again = raw_input ("> ")
#The files opens againg

txt_again = open(file_again)
#you will be able to read the text again
print txt_again.read()

