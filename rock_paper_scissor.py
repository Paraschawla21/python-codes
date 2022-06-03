print("\nWelcome to Rock, Paper and Scissors Game...!!")
your_choice = int(input("\nWhat do you choose? Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
import random
computers_choice = random.randint(0, 2)
if your_choice == 0:
    print("\nYou choose Rock")
    if computers_choice == 0:
        print("\nComputer's choice is also Rock")
        print("\nSo, MATCH IS DRAW...!!\n")
    if computers_choice == 1:
        print("\nComputer choose Paper")
        print("\nSince Paper beats Rock, So, YOU LOOSE...!!\n")
    if computers_choice == 2:
        print("\nComputer Choose Scissors")
        print("\nSince Rock beats Scissors, So, YOU WIN...!!\n")
elif your_choice == 1:
    print("\nYou choose Paper")
    if computers_choice == 1:
        print("\nComputer's choice is also Paper")
        print("\nSo, MATCH IS DRAW...!!\n")
    if computers_choice == 0:
        print("\nComputer choose Rock")
        print("\nSince Paper beats Rock, So, YOU WIN...!!\n")
    if computers_choice == 2:
        print("\nComputer Choose Scissors")
        print("\nSince Scissors beats Paper, So, YOU LOOSE...!!\n")
else:
    print("\nYou choose Scissors")
    if computers_choice == 2:
        print("\nComputer's choice is also Scissors")
        print("\nSo, MATCH IS DRAW...!!\n")
    if computers_choice == 1:
        print("\nComputer choose Paper")
        print("\nSince Scissors beats Paper, So, YOU WIN...!!\n")
    if computers_choice == 0:
        print("\nComputer Choose Rock")
        print("\nSince Rock beats Scissors, So, YOU LOOSE...!!\n")