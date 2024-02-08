number = 10
limited_guess = 5
print("I'm thinking of a number...")
guess = (input("What number am I thinking of? "))

if guess == str(number):
    print("Congratulations! You guessed the right number.")
if guess == 'q':
    print(f'The number was {number}')  
else:
    limited_guess -= 1
    if guess != str(number):
        print(f'You have {limited_guess} left')
    while guess != str(number) and limited_guess <= 5:
        limited_guess -= 1
        guess = (input("Sorry try again. What number am I thinking of? "))
        print(f'You have {limited_guess} left')
        if guess == 'q':
            print(f'The number was {number}')
            break
        if limited_guess == 0:
            print(f'The number was {number}')
            break
        elif int(guess) == number:
            print("Congratulations! You guessed the right number.")
            break
        else:
            if int(guess) < number:
                print('Your guess was too low')
            elif int(guess) > number:
                print('Your guess was too high')
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")


