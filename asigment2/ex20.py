#This will print out the whole text file, and go in to the script
#This will print all of the.
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
#Here the lines will be printed out from the def variables that is written longer up
print "First let's print the whole file:\n"

print_all(current_file)

#Here it will get rewinded, it will go back and rewind the whole thing.
#The current lines gets rewinded.
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)