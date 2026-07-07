#create an rpg game
#player vs enemy
import random
player=input("enter your name:").lower()
enemy=random.choice(['dragon','goblin','troll'])
playerhp=100
enemyhp=100
turn=1
while playerhp>0 and enemyhp>0:
    print(f"{enemy} attacks player")
    enemyhp=enemyhp-random.randint(8,20)
    print(f"player hp{playerhp}")
    print(f"{player} strikes back")
    playerhp=playerhp-random.randint(8,20)
    print(f"enemy hp {enemyhp}")
    turn=turn+1
    if playerhp<=0:
        print("{enemy} won")
        break
    elif enemyhp<=0:
        print("{player} won")