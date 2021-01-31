import datetime
today = datetime.datetime.now()

birth_year = int(input('>What year were you born? '))
age = today.year - birth_year
your_age = f'Your age is {age}'

print(your_age)
# print(type(today.year))