import random

guesses_taken = 0 #assign guesses_taken variable to 0

print('Hello! What is your name?') #welcome message "Hello! What is your name?" on the console screen
myName = input() #assign myName variable to inputed data by user

number = random.randint(1, 20) #assign number variable to random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #print message "Well, ' + myName + ', I am thinking of a number between 1 and 20.", where myName is a variable inputed by the use earlier

while guesses_taken < 6:  #creates a while loop which will repeat until guesses_taken is below 6
    print('Take a guess.') #print message 'Take a guess.' on the console screen
    guess = input()    #assign variable guess into data inputed by the user
    guess = int(guess) #convert guess varible into int type variable

    guesses_taken += 1 #increase the value of the guesses_taken variable by 1

    if guess < number: #if guess is lower then random number it executes an operation below
        print('Your guess is too low.') #print message "Your guess is too low" on the console screen

    if guess > number: #if guess is bigger than random number it executes an operation below
        print('Your guess is too high.') #print message "Your guess is too high" on the console screen

    if guess == number: #if guess is same as random number it executes an operation below
        break #while loop is stopped

if guess == number: #if guess is same as random number it executes an operation below
    guesses_taken = str(guesses_taken) #convert guesses_taken variable into string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #print message "Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!", where myName is a variable inputed by the user, and guesses_taken is a number of guesses

if guess != number: #if guess is not equal to random number it executes an operation below
    number = str(number) #convert randomized number variable into a string type variable
    print('Nope. The number I was thinking of was ' + number) #print "Nope. The number I was thinking of was "" + number, where number is randomized number

