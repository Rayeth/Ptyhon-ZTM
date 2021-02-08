import sys
import random

sys.argv

# to define parameters in terminl
start = int(sys.argv[1])
stop = int(sys.argv[2])

num = random.randint(start, stop)


#x = input(f'>Guess the number between {start} and {stop} \n ')

while True:
    try:
        x = int(input(f'>Guess the number between {start} and {stop} \n '))
        if (start - 1) < x < (stop + 1):
            if x == num:
                print("You've guessed!!!!")
                break
            else:
                print("Try another one!")
                continue
        else:
            print(f"Please enter a number from between {start} and {stop} \n ")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

