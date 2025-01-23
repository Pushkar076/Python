letter = '''Dear<|NAME|>,
you are selected!

date : <|DATE|>
'''
name = input("enter your  name\n ")
date = input("enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)