# Jeg fikk en feil naar jeg skrev koden med en gang
# Slik jeg ser det sa skyltes det hele med en kommafeil altsa hvor en plasserer komma.

cars = 100
# Det er ikke n0dveding aa bruke 4.0, for det som kommer opp da er at bilen
# kan transportere 120 istedenfor 120.0 

#Kapasiteten i bilene defineres
#Hvor mye plass, hvor mange sjaaf0rer hvor mange passaserer
space_in_a_car = 4.0
drivers = 30
passengers = 90

#Her settes variablene inn
#Hvor mange personer som skal settes inn i hver bil
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Til slutt vil det komme hvor mange biler som er tilgjengelig.
#Her printes det kapasitenen og det vil komme frem at det er 100 biler tilgjengelig.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."





