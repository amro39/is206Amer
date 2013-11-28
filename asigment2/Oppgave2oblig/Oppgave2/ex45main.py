###Here i am importing from the other file ex45
import ex45
from random import randint
 
class CentralCorridor(ex45.Scene): #child of scene, this shows the map and where you start the game
 #The first scene of the game. The scenes under the class centralcoridor
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "Try to put it in the bridge, and blow the ship up after getting into an "
        print "This are your options shoot!, dodge! tell a joke" #I added options here to give a hint. 
      
        action = raw_input("> ")
 
        if action == "shoot!": #Here is what happens if you enter shoot! else if is used here, becouse you have several options and the outcome will be what you type in.
            print "Quick on the draw you try to be a hero and you blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim.  Your laser hits his costume but misses him entirely.  This"
            print "completely ruins his brand new costume his mother bought him, which"
           
            return 'death'
 
        elif action == "dodge!": #Here is what happens when you enter dodge! 
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
           
            return 'death'
 
        elif action == "tell a joke": #Here is the final option if you write this option you can go over to the next option
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            
            return 'laser_weapon_armory'
 
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
			
class LaserWeaponArmory(ex45.Scene): #importing from ex45 a scene

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container.  There's a keypad lock on the box"
        print "Your options are hint or guess the code"
       
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) #will randomly choose between number 1,9. The cod will have to be 3 numbers.
        guess = raw_input("[keypad]> ")
        guesses = 0
        if guess == "hint": ##I have added a hint code in this game because it is impossible to guess the code. What it does it gives you the code! Just write hint
		    print code
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
		
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'



class TheBridge(ex45.Scene): #The class of the bridge scene

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
      

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
       
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge" #It will return an escape pod and you will be able to get to the next level when you enter the correct code


class EscapePod(ex45.Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
    
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ") #Here you have to choose a random number from (1,5) This number is always random so its hard to guess right
       
        
        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
         
            print "time.  You won!"


            return 'finished'
			
class Map(object): #This is the class for all the maps in the game. Where you go from one part to another

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': ex45.Death()
    }

    def __init__(self, start_scene): #methods for jump to the next scene
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
		
a_map = Map('central_corridor')
a_game = ex45.Engine(a_map)
a_game.play()