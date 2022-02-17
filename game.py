import random
import wordList
import stages

print('''  
    __________
     |/      |
     |     (o‿o)
     |      \|/
     |       |
     |      | |
     |
    _|___
      
      ''')

print("\nWelcome to Hangman!\n")

chosenWord = random.choice(wordList.wordList)

print(
    "A random word has been chosen from the list. You have 7 guesses to find out the word. Good luck!\n"
)

lives = 7

# Creating blank spaces for the chosen word
display = []
for _ in range(len(chosenWord)):
    display += ["_"]
print(display)

win = False

while not win:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"\nYou already guessed `{guess}`.\n")

    # Checking if the guess is in the word
    for position in range(len(chosenWord)):
        if chosenWord[position] == guess:
            display[position] = guess

    # Handling incorrect guesses
    if guess not in chosenWord:
        lives -= 1
        print(f"\nYour have {lives} lives left.\n")
        if lives == 0:
            print("\nYou lost!\n")
            win = True

    print(f"\n{' '.join(display)}")

    # Checking if the user has won
    if "_" not in display:
        win = True
        print("\nCongratulations! You win!\n")

    print(stages.stages[lives])