first = 0
second = 1

# number is the index of Ficobnacci numbers
def fib(number):

    a = 0
    b = 1

    for item in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(2):
    print(x)



