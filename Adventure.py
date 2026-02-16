import random
row = [''] * 40
print(row)

map_layout = []
for _ in range(40):
    map_layout.append(row.copy())

player = 'X'
map_layout[20][20] = player
current_row = 20
current_column = 20
locations = [
    "You are in a deep dark wood,",
    "You are in a damp tunnel,",
    "You are in a rainforest,",
    "You are in a dry desert,",
    "You are in a festive village,",
]
monsters = [
    'Zombie',
    'Teacher'
    'Dragon',
    'Minotaur',
    'Centaur',
    'Poachers',
]
weapons = [
    'sword',
    'Axe',
    'Bow and arrow',
    'Dynamite',
    'Shotgun',
    'Girl',
    'Shotgun sword axe ',
]
satchel = [
    'potions',
    'food',
    'knife',
    'ingredients'
]
def fight():
    if random.randrange(2) == 1:
        return "You won! "
    return "You lost! "

print("Welcome to adventure")
while True:
    direction = input(f"Which way do you want to go? ")
    if direction == "q":
        exit()
    if direction not in "nsew":
        print("You can't go that way ")
        continue
    if direction == "n" :
        print("Moving north")
        print(current_column,current_row)
        if current_column == 39:
            current_column = random.randrange(0,40)
            current_row = random.randrange(0,40)
            print("You respawned! ")
            continue
        current_column += 1
        print(current_column,current_row)
    elif direction == "e":
        print("Moving east")
        print(current_column, current_row)
        current_row += 1
        print(current_column, current_row)
    elif direction == "s":
        print("Moving south")
        print(current_column, current_row)
        current_column -= 1
        print(current_column, current_row)
    elif direction == "w":
        print("Moving west")
        print(current_column, current_row)
        current_row  -= 1
        print(current_column, current_row)
    print(random.choice(locations))
    enemy_appears = random.randrange(10)
    if enemy_appears == 5:
        print("You are facing an evil enemy")
        result = fight()
        print(result)
    row = random.randrange(0,40)
    column = random.randrange(0,40)
    monster = random.choice(monsters)
    map_layout[row][column] = monster
    print(map_layout)
    for row in map_layout:
        print(row)
