from random import randint
drawn = randint(1,100)
guessed = 0

print("Let's play a game")

while guessed != drawn:
    guessed = int(input("Guess the number from 1 to 100:"))
    if guessed > drawn:
        print("You entered too much value")
    if guessed < drawn:
        print("You entered too low a value")
print("Congratulations!")