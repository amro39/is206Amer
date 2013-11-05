from sys import argv
script, filname = argv

print "Hallo dette er bare en liten test"
print "For aa sjekke om det her fungerer som det skal"

raw_input("?")

print "Opening the file"
target = open(filname, 'w')

print "Sjekke filen"
target.sjekke()

print "Some questions"

line1 = raw_input("Your name?:")
line2 = raw_input("dust eller?:")

print "skal skrive dette her"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print "And finally, we close it."
target.close()



