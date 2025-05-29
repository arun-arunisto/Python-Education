import random

"""
GAME LOGIC
------------
START GAME
↓
Generate a random number
↓
LOOP:
    Ask user for a guess
    ↓
    If guess == number → WIN
    If guess < number → "Too low"
    If guess > number → "Too high"
    ↑ (loop until correct or limit reached)
↓
END GAME (show result and attempts)
"""

def generating_random_number():
    return random.randint(1, 100)

def check_the_integer(guessed_no:int, answer: int):
    if guessed_no > answer:
        if (guessed_no - answer) < 10:
            return False, "Very close, not too high!!"
        return False, "Too high!!"
    elif guessed_no < answer:
        if (answer - guessed_no) < 10:
            return False, "Very close, not too low!!"
        return False, "Too low!!"
    else:
        return True, "You got it!!"

def game():
    attempts = 0
    answer = generating_random_number()
    while attempts < 10:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Invalid, please enter number!!")
            attempts += 1
            print(f"You have {10-attempts} attempts left!!")
            continue
        else:
            result, message = check_the_integer(int(guess), answer)
            if result:                
                print(message)
                print(f"You guessed it in {attempts} attempts!!")
                break
            else:
                print(message)
                attempts += 1
                print(f"You have {10-attempts} attempts left!!")

welcome_message = r"""

  ________                              ___________.__             ________  .__       .__  __   
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____   \______ \ |__| ____ |__|/  |_ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   |    |  \|  |/ ___\|  \   __\
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/   |    `   \  / /_/  >  ||  |  
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > /_______  /__\___  /|__||__|  
        \/            \/     \/     \/                  \/     \/          \/  /_____/           
                                                                        Created by: ARUN ARUNISTO
"""
def main():
    print(welcome_message)
    while True:
        options = input("[1] Start the game [2] Quit the game \nEnter the option: ")
        if options == "1":
            game()
        elif options == "2":
            break
        else:
            print("Invalid option!!")

if __name__ == "__main__":
    main()
