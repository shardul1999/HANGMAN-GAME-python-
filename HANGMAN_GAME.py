import time
from random import randrange

#welcoming the user
name = input("\t HANGMAN GAME"+"\n"+"What is your name? ")

print("Hi " + name.capitalize(), "Let's start the game!")
x=randrange(0,5,1)
print ("")

#wait for 1 second
time.sleep(1)

#print("guess karna shuru kar chal")
guess1 =["adarsh","mahesh","minimart","cricket","hockey"]
#for motivating the players
quote=["Come on!You got this","Good try though","You can do it!"]
word=guess1[x]

#creates an variable with an empty value
guesses = ''

#remaining guesses
remguess = 10
#check if the guesses left are more than zero
while remguess > 0:
    #for characters left count
    charleft = 0

    # for every character in the word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:
            print(char.upper(),end="  ")
        else:
        # to print the number char left
            print("_",end="  ")
            charleft += 1

    # print You Won
    if charleft == 0:
        print("Congrats You won boii!")
        #exit
        break
    print()
    # ask the user to guess a character
    guess = input("Your Guess:")

    # set the players guess to guesses
    guesses += guess
    #for backspace
    bck='\b'
    y=randrange(0,3,1)
    f=quote[y]

    # when character guessed is not present in the word
    if guess not in word:
        remguess -= 1
        print("Wrong",end=" ")
        if remguess>0:
            print(f)
        #show the guesses left
        print("You have " + str(remguess)+" more guesses left")
        print()
        if remguess == 0:

        # user lost
            print("You Lost! Well tried")
    else:
        print()
