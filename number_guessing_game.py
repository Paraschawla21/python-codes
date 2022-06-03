from random import randint # import random
answer = randint(1, 100)   # answer = random.randint(1, 100)
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
def game():
    print("WELCOME TO GUESS A NUMBER GAME..!!")
    print("GUESS A NUMBER BETWEEN 1 AND 100..!!")
    print(f"Pssstt, Correct answer is {answer}")
    def answer_checker(guess, answer):
        if guess > answer:
            print("Too High.")
        elif guess < answer:
            print("Too Low.")
        else:
            print(f"You got it! The answer was {answer}")
    def difficulty():
        difficulty = input("Type 'easy' for easy game or 'hard' for hard game:\n").lower()
        if difficulty == 'easy': # not a good way to take variable name same as function name
            return EASY_ATTEMPTS
        else:
            return HARD_ATTEMPTS
    attempts = difficulty()
    guess = 0 # global but we will make it local cause we have to change it under function
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guess = int(input("Guess a number:\n"))
        answer_checker(guess, answer)
        if attempts == 0:
            print("You ran out of attempts, You loose the game..!!")
            return
game()