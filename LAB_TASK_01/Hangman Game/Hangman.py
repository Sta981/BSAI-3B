# Hangman Game 
'''
1. Get a phrase to guess (from user).
2. turn input into underscores to show letters to be guessed.
3. User guesses letters .
4. Check if letters exist phrase.
5. If letters don't exist in phrase, add a body part to hangman.
6. If letters doexist in phrase,  reveal these letters to user, and update our phrase

'''
import random
def hangman():

    list_words = ["Sticker","Billu","Syed","Tahir","Ali","Nalain","Abass","Meeshiii","Hacker"]
    word = random.choice(list_words).lower()
    turns = 10
    guessmade = ''
    entries = "abcdefghijklmnopqrstuvwxyz"

    while turns >0:

        main_word = ""
        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + '_ '

        if main_word.replace(" ", "") == word:
            print("You Won!.")
            break
        print("Guess the word", main_word) 
        guess = input("Enter a letter: ").lower()
        if guess in entries and len(guess) == 1:
            if guess in guessmade:
              print(" You already guessed that letter! Try something else.")
              continue
            else:
              guessmade = guessmade + guess
        else:
            print("Enter Valid char")
            guess = input().lower()
        if guess not in word:
            turns =turns - 1
            if turns == 9:
                print("9 turns are left.!!")
                print("--------------------")
            if turns == 8:
                print("8 turns are left.!!")
                print("--------------------")
                print("         O         ")
            if turns == 7:
                print("7 turns are left.!!")
                print("--------------------")
                print("         O         ")
                print("         |         ")
            if turns == 6:
                print("6 turns are left.!!")
                print("--------------------")
                print("         O         ")
                print("         |         ")
                print("        /          ")
            if turns == 5:
                print("5 turns are left.!!")
                print("--------------------")
                print("         O         ")
                print("         |         ")
                print("        / \        ")

            if turns == 4:
                print("4 turns are left.!!")
                print("--------------------")
                print("         O/         ")
                print("         |         ")
                print("        / \        ")

            if turns == 3:
                print("3 turns are left.!!")
                print("--------------------")
                print("        \O/        ")
                print("         |         ")
                print("        / \        ")
            if turns == 2:
                print("2 turns are left.!!")
                print("--------------------")
                print("        \O/  |     ")
                print("         |         ")
                print("        / \        ")
            if turns == 1:
                print("1 turns are left.!!")
                print("--------------------")
                print("        \O/__|     ")
                print("         |         ")
                print("        / \        ")
            if turns == 0:
                print("0 turns are left.!!")
                print("--------------------")
                print("        \O/__|     ")
                print("         |         ")
                print("        / \        ")
                print("-------      --------")
                print("You Lose .!!!")
                print("You let a die a a good person")
                break



     

name = input("Enter the player name:")
print(f"Welcome {name}. Thsi is a hangman game.")
print("Guess the number in less than 10 attempts")
hangman()