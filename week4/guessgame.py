import random
num = random.randint(1, 9)
ran = int(input('Welcome to the GUESSING GAME.  Guess a number between 1 to 9: '))
while num != 'ran':
    print
    
    if ran < num:
        print ('Sorry, your number is  to low! Try again.')
        ran = int(input('Guess a number between 1 to 9: '))
    
    elif ran > num:
        print ('Sorry, your number is to low! Try again.')
        ran = int(input('Guess a number between 1 to 9: '))
    
    else:
        print ('Congratulations you won! You guessed the number correctly.  Come back again!')
       
        break
    
    print