
while True:
    try:
        age = int(input(">What is your age?"))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        break
    # used for e.g logs
    finally:
        print('ok, i am finally done')


        # to rasie me own error
        #raise ValueError('my own error') 