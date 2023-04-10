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

import random

rps = [rock, paper, scissors]

your_choice = input("What do you chose? Type 0 for rock, 1 for paper or 2 for scissors\n")
if your_choice == "1" or your_choice == "2" or your_choice == "0" :
  your_choice = int(your_choice)
  print(rps[your_choice])
  print("Computer chose :")
  random_num = random.randint(0,2)
  computer_chose = rps[random_num]
  print(computer_chose)

  if (your_choice == 0 and random_num == 2) or (your_choice == 1 and random_num == 0) or (your_choice == 2 and random_num == 1) :
    print("You won")
  elif (your_choice == 0 and random_num == 1) or (your_choice == 1 and random_num == 2) or (your_choice == 2 and random_num == 0) :
    print("You lost")
  else :
    print("It's a tie")
    
else: 
  print("Invlaid input")