import shutil
import string
import os

dict = {}
i = 1

for char in string.ascii_lowercase + string.ascii_uppercase:
    if char == 'A':
        i -= 26
    dict[char] = i
    i += 1
    
dict['.'] = i
dict[' '] = i+1

text = input("Please enter the text you would like to convert to images: ")
try:
    shutil.rmtree('userinput')
except:
    print("Creating folder: userinput")
os.makedirs('userinput', exist_ok=True)
i = 1
for char in text:
    try:
        source = f'{dict[char]}.jpg'
        renamed = f'userinput/{i}.jpg'
        shutil.copy(source, renamed)
        i+=1
    except:
        print(f"{char} does not have a matching image, please try again.")
