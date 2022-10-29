
# import random
# import string

# # prints abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# letters = string.ascii_letters 
# # print(letters)

# # prints 0123456789
# numbers = string.digits 
# # print(numbers)

# # prints !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# signs_and_symbols = string.punctuation 
# # print(signs_and_symbols)

# combination = letters + numbers + signs_and_symbols
# #print(combination) # class 'str'

# # '' is an empty string
# password = '' 

# while len(password) < 10:
#     password = password + random.choice(combination) 

# print(f'Your password {password}')


# """
# ANOTHER METHOD OF GENERATING PASSWORD 
#  """
# # import random
# # import string

# # # prints abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# # letters = string.ascii_letters 
# # # print(letters)

# # # prints 0123456789
# # numbers = string.digits 
# # # print(numbers)

# # # prints !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# # signs_and_symbols = string.punctuation 
# # # print(signs_and_symbols)

# # combination = letters + numbers + signs_and_symbols
# # #print(combination) # class 'str'

# # random_password = random.choices(combination, k=10)
# # password_combination = "".join(random_password)
# # print()
# # while True:
# # 	print(f'Your password: {password_combination}')
# # 	break


n = 56 % 10
print (n)