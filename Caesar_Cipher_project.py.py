print("""
  _____                         _____ _       _               
 / ____|                       / ____(_)     | |              
| |     __ _  ___  ___  __ _  | |     _ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | | |    | | '_ \| '_ \ / _ \ '__|
| |___| (_| |  __/\__ \ (_| | | |____| | |_) | | | |  __/ |   
 \_____\__,_|\___||___/\__,_|  \_____|_| .__/|_| |_|\___|_|   
                                       | |                    
                                       |_|                    
""")

print("""
=================================================
        🔐 CAESAR CIPHER ENCRYPTION 🔐
=================================================
      A → D    B → E    C → F    D → G
      E → H    F → I    G → J    H → K

          ENCODE • DECODE • SECURE
=================================================
""")


alphabate = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']




def caesar(choice,original_text,shift):
    
    massage = ""
    for x in original_text:
        if x not in alphabate:
             massage+=x
        else:
            place = alphabate.index(x)
            
            if choice == "encode":
                    place+=shift
            elif choice == "decode":
                    place-=shift
            else:
                 print("Please enter 'encode' or 'decode'")
            if place > len(alphabate):
                place % len(alphabate)
            
            n= alphabate[place]
            massage+= n

    if choice == 'encode':
        print(f"Here is your encode massage {massage}")
    elif choice == 'decode':
        print(f"Here is your decode massage {massage}")


game_continue = True

while game_continue:
    diraction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user = input("Type your massage:\n").lower()
    try:
        ac = int(input("Type the shift number:\n"))
    except ValueError:
        print("Please inter number")
    caesar(choice=diraction,original_text=user,shift=ac)

    choice = input("Type 'yes' if you want to go again otherwise type 'no'\n ")
    if choice == 'no':
         game_continue = False
         print('Good bye!')
    elif choice == 'yes':
         game_continue = True
    else:
         print("You entered invalid value")