import random

def guess_the_number():
    print("🎲 Welcome to the Guess the Number Game! 🎲")
    print("Choose difficulty level:")
    print("1. Easy (Unlimited attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")

    # Difficulty selection
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice not in [1, 2, 3]:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Attempts based on difficulty
    if choice == 1:
        attempts = float("inf")  # unlimited
    elif choice == 2:
        attempts = 10
    else:
        attempts = 5

    # Random number
    n = random.randint(1, 20)
    guess_count = 0

    while guess_count < attempts:
        try:
            a = int(input("👉 Enter your guess (1-20): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        guess_count += 1

        if a == n:
            print(f"🎉 Correct! You guessed {n} in {guess_count} attempts.")
            break
        elif a > n:
            print("🔽 Lower number please.")
        else:
            print("🔼 Higher number please.")

        if attempts != float("inf"):
            print(f"💡 Attempts left: {attempts - guess_count}")

    else:
        print(f"😢 Game Over! The correct number was {n}.")

# Replay option
while True:
    guess_the_number()
    play_again = input("🔄 Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye!")
        break