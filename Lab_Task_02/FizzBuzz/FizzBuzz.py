print("Welcome to the Fizz Buzz Game")
player = input("Enter your name:")
instructions = '''
1. Type 'Fizz' for multiples of 3,
2.'Buzz' for multiples of 5, 
3.'FizzBuzz' for multiples of both.
4. Otherwise, just type the number itself.
5. One wrong guess and the game is over!.
6. Survive all 100 rounds to win!.
'''
print(f"Welcome {player}!, There are the instructions. {instructions}")
import random
t = 0
prev_num = 0
while True:

    n = random.randint(1, 20)
    t = prev_num + n  
    prev_num = n           
    

    if t % 3 == 0 and t % 5 == 0:
        c = "fizzbuzz"
    elif t % 3 == 0:
        c = "fizz"
    elif t % 5 == 0:
        c = "buzz"
    else:
        c = str(t)
    

    print(n)  
    guess = input("Your answer: ").lower()
        
    if guess != c:
        print(f"Wrong! The correct answer was {c}. Game Over!")
        break
else:
    print("Congratulations! You Won")

