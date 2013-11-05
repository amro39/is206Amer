name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky
print "If I add %d, %d, and %r I get %r." % (age, height, weight, age + height + weight)

inches = 74
centimeters = inches * 2.54
print "%r inches equals %r centimeters." % (inches, centimeters)

pounds = 180
kilos = pounds * 0.045359237
print "%r pounds equals %r kilos." % (pounds, kilos)

