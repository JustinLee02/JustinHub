import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]

userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
computerChoice = list[random.randint(0,2)]
print(f"Computer : \n {computerChoice}")
print(f"User : \n {list[int(userChoice)]}")
if computerChoice == rock:
    if userChoice == '0':
        print("Draw")
    elif userChoice == '1':
        print("You Win.")
    else:
        print("You lose.")
elif computerChoice == paper:
    if userChoice == '0':
        print("You lose.")
    elif userChoice == '1':
        print("Draw")
    else:
        print("You win")
else:
    if userChoice == '0':
        print("You win.")
    elif userChoice == '1':
        print("You lose.")
    else:
        print("Draw")