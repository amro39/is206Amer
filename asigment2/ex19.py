#Here it will count the amount of cheeses and crackers
#It will say how much you have
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#The amount that is here gets printed out
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# The cheeese and crackers are defined up there and it will
#print out again a new amount of cheese and crackers.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#Here it takes everything togehter combines it an calculate from the whole
#Script, you will get an amunt of over all cheese and boxes of crackers.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Here one will be asked to write in an aount of cheese and crackers
#When you write in the amount in the shell it will calcualte, how much cheese and crakers you have based on what you wrote.
print 'We can assign the function to a variable and simply call it by its new name'
foo = cheese_and_crackers
foo(20,30)

print 'We can call the function in a loop, calling it 10 times'
for i in range(10):
    cheese_and_crackers(20,30)

print 'We can pass a function as arguments.'
print 'We can now ask the user for the number of cheese and crackers'
cheese_and_crackers(int(raw_input('how many cheese?')), int(raw_input('how many crackers?')))


