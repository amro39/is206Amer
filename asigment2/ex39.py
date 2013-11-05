# create a mapping of state to abbreviation

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	
	}
	
#Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
	
	}
	
# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities

print '-' * 10
print "NY States has: ", cities['NY']
print "OR States has: ", cities['OR']

#Print some states
print '-' * 10
print "Michigan's abberviation is. ", states['Michigan']
print "Florida's abberviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
	state, abbrev, cities[abbrev])
	
	print '-' * 10
	#safetley get abbreviation by state that might not be there
	state = states.get('Texas', None)
	
	if not state:
		print "Sorry, no Texsas."
		
	#get a city with a default value
	
	city = cities.get('TX', 'Does Not Exist')
	print "The city for the state 'TX' is: %s" % city
	



	