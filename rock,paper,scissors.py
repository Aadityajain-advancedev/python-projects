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
images=[rock,paper,scissors]
user_choice=int(input("type 0 for rocks, 1 for paper and 2 for scissors"))
print(f"you chose{images[user_choice]}")
computer_choice=int((random.randint(0,2)))
print (f"computer choose :- {images[computer_choice]}")

if user_choice>= 3  or user_choice< 0:
    print("you gave an inappropriate number, you lose")
elif user_choice==2 and computer_choice==0:
    print("you lose")
elif user_choice == 0 and computer_choice == 1:
    print("you lose")
elif user_choice==1 and computer_choice==2:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")

elif user_choice>computer_choice:
    print("you win")

elif user_choice==computer_choice:
    print("it's draw")



