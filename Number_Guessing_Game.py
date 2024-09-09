import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    secret_number = random.randint(1,100)
# Initilize Attempts Count
    attempts = 0
    while True:
        try: 
            guess = int(input("Guess Number Between 1 nad 100: "))

            attempts +=1 
            if guess < secret_number:
                print("Too Low, Try Again: ")
            elif guess > secret_number:
                print("Too high, Tyry Again: ")
            elif guess == secret_number:
                print(f" Congradulations! You have Guessed Correct Number {secret_number} in {attempts} attempts.")
            else:
                print("Invalid Number: Choose a Number between 1 and 100.")
        except ValueError:
            print("InValid Input: Please Choose a Valid Number Between 1 and 100!")

if __name__ == "__main__":
    number_guessing_game()
        
