import random

#list of words
word_bank = [
    {"word": "python", "hint": " A popular programming language"},
    {"word": "hangman", "hint": " The name of this game"},
    {"word": "developer", "hint": " A person who writes code"},
    {"word": "batman", "hint": " The city of Gotham superhero"},
    {"word": "alan turin", "hint": " The father of computer science"},
    {"word": "internet", "hint": " You're probably using it right now"},
]

chosen = random.choice(word_bank)
word = chosen["word"]
hint = chosen["hint"]

guessed_letters = []
wrong_guesses = 0
attempts = 6

print("Welcome to Hangman!")
print(f" Hint{hint}")

while wrong_guesses < attempts:
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("\nWord:", " ".join(display))

    if "_" not in display:
        print("Congratulations! You guess the word")
        break

    guess = input ("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Nice guess")
    else:
        wrong_guesses +=1
        print(f"Wrong! you have {attempts - wrong_guesses} attempts remaining.")

if wrong_guesses == attempts:
    print("\nGame Over!")
    print(f"The word was {word}")





