people = 60
cars = 90
buses = 25


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
	
if people < buses and buses < cars:
    print "This buss wont drive."
else:
    print "This car will drive."

if buses == people or people > cars:
    print "This bus won't drive."
else:
    print "This car will drive."
