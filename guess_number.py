number = 10

print("I'm thinking of a number...")
guess = (input("What number am I thinking of? "))

if guess == str(number):
    print("Congratulations! You guessed the right number.")
if guess == 'q':
    print(f'The number was {number}')  
else:
    while guess != str(number):
        guess = (input("Sorry try again. What number am I thinking of? "))
        if guess == 'q':
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


