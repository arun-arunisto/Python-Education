from words_list import words_list
import random
"""
Start Game
↓
Pick a random word
↓
Scramble the word
↓
Display scrambled word
↓
Ask for player’s guess
↓
If correct → Congratulate
If wrong → Ask again
↓
Option to play again or quit
↓
End Game
"""
def get_random_word(li: list):
    return random.choice(li)

def scramble_word(word: str):
    return "".join(random.sample(word, len(word)))

def scramble_logic():
    tries = 1
    actual_word = get_random_word(words_list)
    scrambled_word = scramble_word(actual_word)
    print(scrambled_word)
    while tries <= 3:
        guess = input("Enter the actual word: ")
        if guess.lower() == actual_word:
            print("Congrats!!! You guessed it right!!🎉")
            break
        print("You have", 3-tries, "tries left!!")
        tries += 1
        if tries > 3:
            print("You lost the game!! The actual word was:", actual_word)
            break
def play_game():
    while True:
        options = input("[1] Start the game [2] Quit the game \nEnter the option: ")
        if options == "1":
            scramble_logic()
        elif options == "2":
            print("Thank you for playing!! 👋")
            break
        else:
            print("Invalid option!!")

welcome_text = r"""
                                                           created by: ARUN ARUNISTO
                        .___                                      ___.   .__          
__  _  _____________  __| _/ /\   ______ ________________    _____\_ |__ |  |   ____  
\ \/ \/ /  _ \_  __ \/ __ |  \/  /  ___// ___\_  __ \__  \  /     \| __ \|  | _/ __ \ 
 \     (  <_> )  | \/ /_/ |  /\  \___ \\  \___|  | \// __ \|  Y Y  \ \_\ \  |_\  ___/ 
  \/\_/ \____/|__|  \____ |  \/ /____  >\___  >__|  (____  /__|_|  /___  /____/\___  >
                         \/          \/     \/           \/      \/    \/          \/ 

"""
if __name__ == "__main__":
    print(welcome_text)
    play_game()