logo = """
\033[1;33m
╔══════════════════════════════════════════════╗
║                                              ║
║      💰  BLIND AUCTION SYSTEM  💰           ║
║                                              ║
║          🏆 HIGHEST BID WINS 🏆             ║
║                                              ║
╚══════════════════════════════════════════════╝
\033[0m

\033[1;32m
      ____________________________
     /                           /|
    /   PLACE YOUR SECRET BID   / |
   /___________________________/  |
   |                           |  |
   |      $$$$$$$$$$$$$$       |  |
   |      AUCTION BOX 📦       |  |
   |      $$$$$$$$$$$$$$       |  /
   |___________________________| /
   |___________________________|/
\033[0m

\033[1;36m
██████╗ ██╗     ██╗███╗   ██╗██████╗
██╔══██╗██║     ██║████╗  ██║██╔══██╗
██████╔╝██║     ██║██╔██╗ ██║██║  ██║
██╔══██╗██║     ██║██║╚██╗██║██║  ██║
██████╔╝███████╗██║██║ ╚████║██████╔╝
╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝

 █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
\033[0m
"""

print(logo)


def find_highest_bidder(bid):
    high = 0
    name = ""
    for x in bid:
        score = bid[x]
        if score > high:
            high =score
            name = x
    print(f"The winner is {name} with a bid of ${high}")

bidder = {}
should_continue = True
while should_continue:
    user = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bidder[user] = bid
    
    other = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if other == 'no':
        find_highest_bidder(bid=bidder)      
        should_continue = False
    elif other == "yes":
        print("\n"*30)
        should_continue = True
    else:
        print(f"You entered invalid {other} input Try again!")
        should_continue = False
    

