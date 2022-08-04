import string
import random


how_many_chars = int(input("How many characters do you want your Password to have? Range 4-16 "))
if how_many_chars <= 3 or how_many_chars >=17:
    print("Password Generator can only generate password from Range 4-16")
    quit()

length_of_password = how_many_chars
password = ""

nums_to_generate = random.randint(1,(int(length_of_password) - 3))
numbers = random.sample(range(0,9),nums_to_generate)
for i in numbers:
    password += str(i)

length_of_chars = length_of_password - (len(password) + 2)
character_list = (list(string.punctuation))
chars_to_generate = random.randint(1,length_of_chars)
characters = random.sample(character_list, chars_to_generate)

for i in characters:
    password += str(i)

length_of_lower = length_of_password - (len(password) + 1)
lower_alpha_list = list(string.ascii_lowercase)
lower_alpha_to_generate = random.randint(1,length_of_lower)
small_letters = random.sample(lower_alpha_list, lower_alpha_to_generate)

for i in small_letters:
    password += str(i)

length_of_upper = length_of_password - len(password)
upper_alpha_list = list(string.ascii_uppercase)
upper_alpha_to_generate = length_of_upper
big_letters = random.sample(upper_alpha_list, upper_alpha_to_generate)

for i in big_letters:
    password += str(i)

password = ''.join(random.sample(password,len(password)))    
print(password)     
print(len(password))

password_safe =  open('password_safe.txt','a')
password_safe.write(password + "/n")
password_safe.close

