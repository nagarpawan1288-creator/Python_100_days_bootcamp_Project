import random
stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

new_stage = stages[::-1]

words = [
    "ability", "account", "achieve", "action", "adventure",
    "ancient", "animal", "answer", "balance", "beautiful",
    "benefit", "brilliant", "capture", "careful", "challenge",
    "choice", "complete", "creative", "culture", "curious",
    "decision", "develop", "discover", "education", "effort",
    "energy", "example", "experience", "explore", "favorite",
    "freedom", "friendship", "future", "generous", "harmony",
    "history", "imagine", "improve", "journey", "knowledge",
    "language", "learning", "memory", "opportunity", "patience",
    "respect", "success", "support", "victory", "wisdom"
]



copmuter =  random.choice(words)


space = ""
for char in copmuter:
    space+="_"
print(space)



correct_word = []

lives = 6
game_over = True
while game_over:
   print(f"*****************You have left {lives}/6******************")
   placeholder = ""
   user = input("guess a letter\n").lower()
   if user in correct_word:
       print(f"You've already guessed {user}")
   for x in copmuter:
       if user == x:
          placeholder+=x
          correct_word.append(x)
       elif x in correct_word:
           placeholder+=x
       elif not user in x:
           placeholder+="_"
   print(placeholder)
   if user not in copmuter:
       lives-=1
       print(f"You guessed {user}, that's not in the word. You lose a life")
       print(new_stage[lives])
       if lives ==0:
           game_over = False
           print("************You lose***************")
           print(f"It was {copmuter} correct word")

   if "_" not in placeholder:
       print("*************🏆🏆You won!🏆🏆*************")
       print(f"It was {copmuter} correct word! ")
       game_over = False






