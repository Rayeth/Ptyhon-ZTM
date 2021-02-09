import re

pattern = re.compile(r'[A-Za-z0-9$%#@]{7,}[0-9]')

password = 'aasasasasasaj$#'

#a = pattern.search(string)
check = pattern.fullmatch(password)

print(check)

