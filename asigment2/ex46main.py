class LaserWeaponArmory(Scene):

def enter(self):
	print"You have enterd a fighithing sone"
	print "What do you prefer to do in this zone"
	
	action = raw_input("> ")
	
	if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			return 'death'
			
			elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
			return 'death'
			  elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
			return 'laser_weapon_armory'
			
			else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
			
			class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
		 while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
			 if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
			else:
            print "The lock buzzes one last time and then you hear a sickening"
			class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
		 action = raw_input("> ")
		 
		 if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
			 return 'death'
			 elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
			 return 'escape_pod'
			   else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
			 
			 class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
		
		 good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
			return 'death'
  else:
            print "You jump into pod %s and hit the eject button." % guess
			return 'finished'
			
			class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
		
		a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()