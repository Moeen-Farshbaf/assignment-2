import random
dice_active = True
turn_active = True
while dice_active:
    

        
    player_says = input("Enter 'roll' to roll the dice:\n"+"if it's a 6 you'll get to roll again.")
        
    dice = random.randint(1,6)
    
        
    if player_says == 'roll':
        print ("Your number is; "+str(dice))
        if dice == 6:
            
            print("You can roll again.")
        elif dice != 6:
            turn=input("Pass the phone to next player and type 'next'. or if you are done type 'done'")
            if turn == 'done':
                dice_active = False



