print("WELCOME TO NUMBER GUESSING GAME")

secret_number = 7
attempts = 3

while attempts > 0:

    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Congratulations! You won.")
        break

    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts left:", attempts)

for i in range(attempts):
    print("Keep Practicing!")

if attempts == 0:
    print("Game Over!")
    print("The correct number was:", secret_number)