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
        if int(guess) == number:
                print("Congratulations! You guessed the right number.")


