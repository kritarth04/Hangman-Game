import os
import time
import random

name = input("Enter your name → ")
os.system('cls')
print('\nWelcome',name.title())
print("_____________________________________________________________________________________\n")

print("Instructions\n1- Try to guess the spelling.\n2- You only have 10 lives ❤️ ","\n")

def hangman():
    word = random.choice(['executioner','headsman','murderer','executor','assassin','killer','butcher','deathsman','nihilism','existentialism'])
    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print('!! Congratulations !!'.center(175))
            print("You Win".center(175))
            break

        print("Guess the word:" , main)
        guess = input("→ ")

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input("→ ")

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print(r"9 turns left")
                print(r"  --------  ")
            if turns == 8:
                print(r"8 turns left")
                print(r"  --------  ")
                print(r"     O      ")
            if turns == 7:
                print(r"7 turns left")
                print(r"  --------  ")
                print(r"     O      ")
                print(r"     |      ")
            if turns == 6:
                print("6 turns left")
                print(r"  --------  ")
                print(r"     O      ")
                print(r"     |      ")
                print(r"    /       ")
            if turns == 5:
                print(r"5 turns left")
                print(r"  --------  ")
                print(r"     O      ")
                print(r"     |      ")
                print(r"    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print(r"   \ O      ")
                print(r"     |      ")
                print(r"    / \     ")
            if turns == 3:
                print(r"3 turns left")
                print(r"  --------  ")
                print(r"   \ O /    ")
                print(r"     |      ")
                print(r"    / \     ")
            if turns == 2:
                print(r"2 turns left")
                print(r"  --------  ")
                print(r"   \ O /|   ")
                print(r"     |      ")
                print(r"    / \     ")
            if turns == 1:
                print(r"1 turns left")
                print(r"Last breaths counting, Take care!")
                print(r"  --------  ")
                print(r"   \ O_|/   ")
                print(r"     |      ")
                print(r"    / \     ")
            if turns == 0:
                print(r"You loose")
                print(r"You let a kind man die")
                print(r"  --------  ")
                print(r"     O_|    ")
                print(r"    /|\      ")
                print(r"    / \     ")
                break

hangman()