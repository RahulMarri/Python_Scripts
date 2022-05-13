#Guessing Game Challenge
#The Challenge:

#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is
#within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"
#On all subsequent turns, if a guess is
#closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"
#When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!


import random
x = random.randint(1,100) #Generating a random integer in the range of (1,100)

#Intro to the Game and Rules

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

#List to store the guesses
guesses = [0]

#while loop for a valid guess
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess?"))

    if guess<1 or guess>100:    #number should be in range of 1 to 100
        print('OUT OF BOUNDS!! Please Try again: ')
        continue
#comparing guess to the number
    if guess == x:
        print(f" guessed the num correctly in {len(guesses)}!")
        break
#if the guess is incorrect, we append it to the guesses list
    guesses.append(guess)
#when testing the first guess, guesses[-2]==0, which evaluates to false
    if guesses[-2]:
        if abs(x-guess) < abs(x-guesses[-2]):
            print("WARMER")
        else:
            print("COLDER!!")
    else:
        if abs(x-guess)<=10:
            print("WARM")
        else:
            print("COLD!")
