import random

words = ['telephone', 'spongebob', 'house', 'hangman', 'program', 'python']

def letter_input(available_guesses):
    letter = input(f'Guess a letter ({available_guesses} guesses available): ')
    return letter

def board_update(word, board, letter):
    if letter in word:
        count = word.count(letter)
        a = 'is' if count == 1 else 'are'
        letters_var = 'letter' if count == 1 else 'letters'
        print(f"Yes, there {a} {count} {letters_var} '{letter}':")
        for i,item in enumerate(word):
           if letter == item:
               board[i] = letter
    else:
        print(f"No, the letter '{letter}' is not in my word")
    return board

def main(words):
    print('I am thinking of a word. What word is it?: ')
    word = random.choice(words)
    available_guesses = round(len(word) * 1.5)
    board = ['_'] * len(word)
    print(' '.join(board))
    while True:
        letter = letter_input(available_guesses)
        available_guesses -= 1
        print(' '.join(board_update(word, board, letter)))
        if available_guesses == 0 and '_' in board:
            print(f"You lost, the word was '{word}'")
            break
        elif '_' not in board:
            print('You win!!!')
            break

main(words)