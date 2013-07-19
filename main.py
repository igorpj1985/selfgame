import random

class character:
    def __init__(self, id):
        self.id = id
        self.load(self.id)
    def load(self, id):
        self.name = ''
        self.exp = 0
        self.hp = 10
        self.str = 1
        self.crit = 0.2



def fight(player1, player2):
    while 1:
        print player1.name, "[HP:", player1.hp, "]"
        print player2.name, "[HP:", player2.hp, "]"
        kick(player1, player2)
        if player2.hp <=0:
            return player1
        kick(player2, player1)
        if player1.hp <=0:
            return player2
        print "----------"

def kick(player, target):
    print player.name, "kick", target.name
    target.hp = target.hp - player.str

def chance(chance): #chance 0.0 - 1.0
    if random.random()*1/(1-chance) >= 1:
        return 1
    else:
        return 0

igor = character(0)
igor.name = "Igor"
pet = character(1)
pet.name = "Pet"

winner = fight(igor, pet)
print "Fight win:", winner.name
print random.random()
