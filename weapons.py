import random
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