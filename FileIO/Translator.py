from translate import Translator

translator= Translator(to_lang="pt")

try:
    with open(r"C:\Users\nopa\OneDrive - H. Lundbeck A S\Desktop\Git\Python-ZTM\FileIO\test.txt", 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open(r"C:\Users\nopa\OneDrive - H. Lundbeck A S\Desktop\Git\Python-ZTM\FileIO\test-en.txt", 'w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as e:
    print('chek your file path silly!')



