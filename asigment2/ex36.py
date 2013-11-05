print "You enter into a house with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There is a monster sitting in the room, ready to kill you what do you do?"
    print "1. run away from the monster."
    print "2. Shoot the monster."

    monster = raw_input("> ")

    if monster == "1":
        print "The monster runs after you and eats you up!"
    elif monster == "2":
        print "The monster falls down dead. Good job!"
    else:
        print "Well, doing %s is probably better.  Momster runs away." % monster

elif door == "2":
    print "You have enterd dreamland what would you like to do in dreamland?."
    print "1. Fly the dragon."
    print "2. Take a run with the dragon through the beatifull landscapre."
    print "3. Start eating cakes the whole day."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "!You fall from the dragon and end up dead!!"
    else:
        print "You end up eating the cake and win the whole game. Good job"

else:
    print "You end up falling down and smash your head, your dead!"