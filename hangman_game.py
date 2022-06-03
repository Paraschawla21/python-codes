word_list = ["ardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print("Pssttt, the solution is")
display = []
for letters in chosen_word:
    display.append("_")
print(display)
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter from the word: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        print(f"\nCurrent position: {position}\nCurrent letter: {letter}\nYour guessed letter is: {guess}")
        if guess == letter:
            display[position] = letter
    print(f"\n{display}")
    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou lost a life, and your remaining lives are {lives}")
        if lives == 0:
            end_of_game = True
            print("YOU LOSE...!!")
    if "_" not in display:
        end_of_game = True
        print("YOU WON...!!")