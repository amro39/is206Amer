#Text Adventure.py
#By Chris O'Leary

global gold
gold=0
def start():
    print '''You find yourself in the foyer of a large house. You
    have no idea how you got there. You look around, and see the front door.
    It is locked and barred, and the bar is nailed down. There is
    no way to open it. There are three other doors in the area. A voice says '50 gold is what you need,
    to escape my grasp, of this take heed!'''
    print
    
def foyer():
    print "Current Gold = ",gold
    print '''You are in the Foyer. The walls are lined with trophy cabinets
    and suits of armour. The exits are (N)orth, (E)ast and (W)est.
    Type 'Help' for a full list of commands.'''
    print
    prompt_foy()
    
def prompt_foy():
    prompt_f = raw_input("Type a command: ")
    if prompt_f == "W":
        reading_room()
    elif prompt_f == "Help":
        print "Look, Examine (Object), N, W, E, S, Take (Item)"
        prompt_foy()
    elif prompt_f == "Examine Armour":
        print "The armour is rusted, and not of any use."
        prompt_foy()
    elif prompt_f == "Examine Cabinet":
        print '''The cabinet is lined with trophies, dating back to the 1800s.
        Seems this was a talented family.'''
        prompt_foy()
    elif prompt_f == "S":
        if gold < 50:
            print "You can't get out untill you have 50 gold."
            prompt_foy()
def reading_room():
    print "Current Gold = ",gold
    print '''You are in an large reading room. The room is stuffed with novels
    and poetry books on every shelf. There is a large table in the middle
    of the room. It has a reading lamp, and a cluster of books scattered about
    on top. The exits are (N)orth and (E)ast. Type 'Help' for a full list of
    commands.'''
    print
    prompt_rea()
    
def prompt_rea():
    prompt_r = raw_input("Type a command: ")
    if prompt_r == "E":
        foyer()
    elif prompt_r == "Help":
        print "Look, Examine (Object), N, W, E, S, Take (Item)"
        prompt_rea()
    elif prompt_r == "Look":
        "You see 30 gold pieces on the table."
        prompt_rea()
    elif prompt_r == "Take Gold":
        print "You get 30 gold!"
        gold = gold+30
        reading_room()
start()
foyer()