
while True:
    try:
        age = int(input(">What is your age?"))
        10/age
    except ValueError:
        print('Please enter a number')
    else:
        break