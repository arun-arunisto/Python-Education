import random
from list_of_words import words_list

stage = {
0:r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
1:r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
2:r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
3:r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
4:r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
5:r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
6:r"""
  +---+
  |   |
  O   |
 /|\  | "Sorry!! He's dead better luck next time"
 / \  |
      |
=========
"""
}

sucess = r"""
  +---+
      |
      |
 \O/  | "You save the day!!"
  |   |
 / \  |
=========
"""

welcome_message = r"""
    _____________
    |         |
    |         0
    |        /|\
    |        / \
    |
    |   
  ___ ___                    Created by: Arun Arunisto                                  
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /     \\__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/ 

"""
def hangman_stages(step: int):
    return stage.get(step)

def get_random_word(li: list):
    return random.choice(li)

def generate_empty_list(word: str):
    return ["_" for i in word]

def index_of_guessed_alphabet(word: str, alphabet: str, guessed_list: list):
    index_li = [i for i, letter in enumerate(word) if letter==alphabet]
    for i in index_li:
        if guessed_list[i] == "_":
            guessed_list[i] = alphabet
            break
    return guessed_list



def game(word: str, empty_li: list):
    step = 0
    while step < 7:
        print(empty_li)
        print(f"Remaning rounds: {7-step}")
        guess = input("Guess the alphabets to fill in the blanks and save the man: ")
        if guess in word:
            index_of_guessed_alphabet(word, guess, empty_li)
            if "_" not in empty_li:
               print(sucess)
               break
        else:
            print(hangman_stages(step))
            step += 1
    print("The answer is:",word)

def main():
    while True:
        options = input("[1] Start the game [2] Quit the game\nEnter the option: ")
        if options == "1":
            word = get_random_word(words_list)
            empty_li = generate_empty_list(word)
            game(word, empty_li)
        elif options == "2":
            break
        else:
            print("Invalid option!!")
if __name__ == "__main__":
    print(welcome_message)
    main()
            
