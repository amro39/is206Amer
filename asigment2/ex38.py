ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things en that list, let's fix that ."
#Here we are adding more stuff to the list above
#Each of this things will be adde seperatly one by one by one, in each line.
#This will actually pring and adding the next one, and then the next one and so on
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
#At the end all that we added will show up one line	
print "There we go: ", stuff

print "Let's do some things with stuff."
#Here we are just printing out by numer
#Longer doen the line the stuff gets joined togehter.
print stuff[1]
print stuff[-1] #fancy
print stuff.pop()
print ' '.join(stuff) #What?? cool!
print '#'.join(stuff[3:5]) #Super stellar!

