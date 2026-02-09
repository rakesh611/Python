import random

# Hangman stages (0 = full life, 6 = game over)
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

# Word list (DevOps tools)
word_list = ["docker", "kubernetes", "ansible", "jenkins", "linux", "python"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length
lives = 6
guessed_letters = []

print("🎮 Welcome to HANGMAN (DevOps Edition)")
print(stages[0])

# SIMPLE display
print("Word:", end=" ")
for letter in display:
    print(letter, end=" ")
print()

# Game loop
while lives > 0 and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct guess!")
    else:
        lives -= 1
        print("❌ Wrong guess!")

    print(stages[6 - lives])

    # SIMPLE display again
    print("Word:", end=" ")
    for letter in display:
        print(letter, end=" ")
    print()

    print(f"Lives left: {lives}")

# Result
if "_" not in display:
    print("\n🎉 Congratulations! You WON!")
    print("The word was:", chosen_word)
else:
    print("\n💀 GAME OVER!")
    print("The word was:", chosen_word)
