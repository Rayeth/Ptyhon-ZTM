username = input('>Type your username ')
password = input('>Type your password ')
pass_lenght = len(password)
encrypted_password = pass_lenght * '*'


print(f'{username}, your password {encrypted_password} is {pass_lenght} letters long')