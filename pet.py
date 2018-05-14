import random
from random import randint

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.health = 50
        self.ascend = False

    def eat(self):
        print(self.name + " say mmmmmm so tasty!")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def play(self):
        print("yippee!")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self, n):
        if self.direction == 0:
            self.y += n
        elif self.direction == 1:
            self.x += n
        elif self.direction == 2:
            self.y -= n
        elif self.direction == 3:
            self.x -= n

    def dab_on(self, other):
        print(self.name + " dabs on " + other.name + "! sick!")

    def agr(self):
        print(self.name + " jams out to Ain't Got Rhythm " \
              + "by the drummer from 80s band Love Handel. cool!") 

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    def hug(self, other):
        other.health += 10
        print(self.name + " hugs " + other.name +"!! uwu")
        print(other.name + "'s health increases by 10")

        if other.health >= 100:
            other.ascend = True
            print(other.name + " has ascended to the astral plane! owo")

    def attack(self, other):
        damage = random.randint(5, 35)
        other.health -= damage
        print(self.name + " attacks " + other.name + "! O.O")
        print(other.name + "'s health is now " + str(other.health))
              
        
        
        
    
    
pet1 = Pet("jim")
pet2 = Pet("john")
pet3 = Pet("bames")
