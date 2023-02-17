print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


if input('You are on a crossroads. Do you want to go "left" or "right"?\n') == "left" :
  
  if input('You encountered a river. Do you want to "swim" or "wait" for the ferry?\n') == "wait" :
    
    decision = input('You got to the other side safely. You see three doors, "red", "yellow" and "blue". Which one do you choose?\n')
    if decision == "red" :
      print("You stepped into a gate of fire and burned to ash! Game over!\n")
    elif decision == "yellow" :
      print("You showed strength of will and had sheer amount of luck! You win!\n")
    elif decision == "blue" :
      print("Mighty ancient beasts awaited you behind the blue door. You became their breakfast. Game over!\n")
    else:
      print("You were thinkig so hard, that you forgot how to breathe and died! Game over!\n")
      
  else:
    print("You got attacked by a trout and died! Game over!\n")   
    
else:
  print("You have overseen a hole and proceeded to learn, how deep it was (the hard way)! Game over!\n")