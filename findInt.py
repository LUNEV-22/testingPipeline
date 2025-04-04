import random
import sys

tries = 0
number = random.randint(1, 50)

print('Hmmm... Try to guess what number between 1 and 50 I was thinking about :)')

# Получение аргументов из командной строки
guesses = [int(arg) for arg in sys.argv[1:]]

for guess in guesses:
    tries += 1
    
    if guess < number:
        print(f'Your guess {guess} is too low')
        
    if guess > number:
        print(f'Your guess {guess} is too high')
        
    if guess == number:
        print(f'Congratulations! You guessed my number in {tries} guesses.')
        break
        
    if guess != number and tries == 6:
        print(f"Sorry, but you didn't make it. My number was: {number}")
        break
