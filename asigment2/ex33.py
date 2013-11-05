i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	print "The numbers: "
	for num in numbers:
		print num

def init_list(no_elements):
	"""
	return a list with all elements initlized to their index value
	"""
	i = 0
	numbers	= []
	while i < no_elements:
		numbers.append(i)

		i += 1

	# return initialized array
	return numbers


numbers = init_list(7)
print "The numbers: "
for num in numbers:
    print num