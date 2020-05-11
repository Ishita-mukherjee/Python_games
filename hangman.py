import random

def hang():
    words=random.choice(["superman","batman","spiderman","thor","nick fury"])
    turns=10
    valid='abcdefghijklmnopqrstuvwz'
    guessmade = ''
    while len(words)>0:
        main=""
        for letter in words:
            if letter in guessmade:
                main = main+letter   #other times this one
            else:
                main = main+"_"+""  #this loop executes for the first time
        if main==words:
            print (main)
            print("You have won!")
            break
        print("Guess the word",main)
        guess=input()
        if guess in valid:
            guessmade=guessmade+guess
        else:
            print("Enter a valid character")
            guess=input()
        if guess not in words:
            turns=turns-1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break





print("\t\tHANGMAN")
print("-------------------------------------------------")
name = input("Enter your name: ")
print("\t\tWelcome",name,"!")
print("-------------------------------------------------")
print("Try to guess the word in less than 10 attempts.")
hang()
print()
