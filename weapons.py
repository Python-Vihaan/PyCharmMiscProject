import random

from Adventure import locations


class Weapon:
    def __init__(self):
        self.power = 10
    def use(self):
        damage = random.randrange(0,21)
        self.set_power()
        return damage
    def grant_special(self):
        pass
    def set_power(self):
        self.power -= 1

sword = Weapon()
damage = sword.use()
print(damage)
print(sword.power)





class Monster:
    pass


class Locations:
    pass

class Satchel:
    pass

class Player:
    pass
class Map:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.row = [" "] * self.columns
        self.the_map = [self.row.copy() for number in range(self.rows)]
        self.the_map[0][self.columns//2] = "X"
        self.player_location = [0,self.columns//2]
    def move(self,direction):
        self.player_location[self.player_location[0][self.player_location[1]] = " "
        if direction == "u":
            self.player_location[0]+= 1
        elif direction == "d":
            self.player_location[0]-= 1
        elif direction == "l":
            self.player_location[1]-= 1
        elif direction == "r":
            self.player_location[1] -= 1





map = Map(20,20)
while True:
    direction = input("Which direction do you want to move? ")
    map.move(direction)
    for row in map.the_map:
        print(row)

