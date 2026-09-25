import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)  

"""

paper = """
    ______
---'  ____)____
          ______)
          _______)
          _______)
---.__________)

"""

scissors = """
    
    ______
---'  ____)____
          ______)
        __________)
      (____)
---.__(___)

"""


"""rock crush scissors
paper crush rock
scissors crush paper
"""
try:
   user = int(input(("What do you want? for 'Rock' enter 0, 'Paper' enter 1, 'Scissors' enter 2\n")))
except ValueError:
    print("You enter invalid key")

turn = [rock,paper,scissors]
computer = random.randint(0,2)

if user == computer:
    print("Its draw")
    print(f"Computer chose {turn[computer]}")

    print(f"you chose {turn[user]}")
elif user == 1 and computer == 2:
    print("Computer win")
    print(f"Computer chose {turn[computer]}")

    print(f"you chose {turn[user]}")
elif user == 2 and computer == 1:
    print("You win")
    print(f"Computer chose {turn[computer]}")

    print(f"you chose {turn[user]}")
elif user == 0 and computer == 2:
    print("You win")
    print(f"Computer chose {turn[computer]}")

    print(f"you chose {turn[user]}")
elif user== 2 and computer == 0:
    print("You lose!")
    print(f"Computer chose{turn[computer]}")

    print(f",you chose {turn[user]}")
else:
    print("You enter invalid number 'You lose!'")



