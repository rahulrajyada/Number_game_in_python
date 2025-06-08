import random

# Tuple for difficulty levels: (name, max number, max attempts)   # not done me yet
difficulties = (
    ("Easy", 10, 5),
    ("Medium", 50, 7),
    ("Hard", 100, 10)
)

# Display difficulty options
print("Choose Difficulty Level:")
for i, (name, _, _) in enumerate(difficulties):
    print(f"{i + 1}. {name}")

choice = int(input("Enter choice (1/2/3): ")) - 1
level_name, max_number, max_attempts = difficulties[choice]

# Generate random number
secret_number = random.randint(1, max_number)
guesses = []

print(f"\n🎯 I'm thinking of a number between 1 and {max_number}. You have {max_attempts} tries!")

# Game loop
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    guesses.append(guess)

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempt} tries.")
        break
    elif guess < secret_number:
        print("Too low 📉")
    else:
        print("Too high 📈")

else:
    print(f"\n❌ Out of attempts! The number was {secret_number}.")

# Show all guesses
print("\nYour guesses were:", guesses)

