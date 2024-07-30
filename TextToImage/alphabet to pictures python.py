
# This script takes in user input and converts it into pictures in the folder "userinput"
# upper and lowercase letters give the same images, spaces and dots are supported.
# if you type any other character that character won't be converted


import shutil
import string
import os

dict = {}
i = 1

#loop over lower and uppercase methods and map them to numbers
for char in string.ascii_lowercase + string.ascii_uppercase:
    if char == 'A':
        i -= 26
    dict[char] = i
    i += 1

#adding space and dot
dict['.'] = i
dict[' '] = i+1

#getting user input
text = input("Please enter the text you would like to convert to images: ")
try:
    shutil.rmtree('userinput')
except:
    print("Creating folder: userinput")
os.makedirs('userinput', exist_ok=True)
i = 1
# loop over each character in userinput, convert to an image, rename it then copy it to the folder
for char in text:
    try:
        source = f'{dict[char]}.jpg'
        renamed = f'userinput/{i}.jpg'
        shutil.copy(source, renamed)
        i+=1
    # this message will be displayed whenever a character isnt matched
    except:
        print(f"{char} does not have a matching image, please try again.")
