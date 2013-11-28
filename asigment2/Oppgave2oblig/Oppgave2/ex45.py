###Here i cam importing from the other file ex45main.
### I use to files, ex45 and ex45 main. So i am importing ex45 main here
### I have just used the game from learnpython the hard way. Pluss that i have added some extra functions to the game you will see that in the next file

import ex45main

from sys import exit
from random import randint

class Scene(object): 

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
		
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
			
class Death(Scene):

    quips = [
        "You died.",
         "Even my grandma can do beter.",
         "Such a looser.",
         "Is that the best you can do."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
