
print('''  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                      
                                                      
                                                      
                                                      
 ,adPPYba, 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   
a8P_____88 88P'   "88"    "8a ""     `Y8 88P'    "8a  
8PP""""""" 88      88      88 ,adPPPPP88 88       d8  
"8b,   ,aa 88      88      88 88,    ,88 88b,   ,a8"  
 `"Ybbd8"' 88      88      88 `"8bbdP"Y8 88`YbbdP"'   
                                         88           
                                         88      ''')

print("Welcome to Treasure Island.Your mission is to find the treasure")

task1 = input("You're at a cross road. Where do you want to go?Type 'left' or 'right'\n").lower()



if task1 == "right":
    print("You fell into a hole. Game Over.")
elif task1 == "left":
    task2 = input("You've come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if task2 == "swim":
        print("You get attacked by an angry trout. Game over")
    elif task2 == "wait":
        task3 = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?\n")
        if task3 == "red":
            print("It's a room full of fire. Game Over.")
        elif task3 == "yellow":
            print("You found the treasure! ? You Win!")
        elif task3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("you entered invalid choice Game Over.")


