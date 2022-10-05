numerical_ranges = """ 
Numerical Ranges
----------------
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
"""

print(numerical_ranges)

user_guess = input("Enter a number between 1 and 100: ")
user_guess = int(user_guess)

if 90 >= user_guess <= 100:
    print(f'Based on your guess of {user_guess}, you scored an A. Congrats!')
elif 80 >= user_guess <= 89:
    print(f'Based on your guess of {user_guess}, you scored an B. Not too bad my friend!')
elif 70 >= user_guess <= 79:
    print(f'Based on your guess of {user_guess}, you scored an C. Better luck next time my friend!')
elif 60 >= user_guess <= 69:
    print(f'Based on your guess of {user_guess}, you scored an D. Oh dear! do you need help?')
elif 0 >= user_guess <= 59:
   print(f'Based on your guess of {user_guess}, you scored an F. Sorry! See me after this.')
else: 
    print(f'Your guess of {user_guess} is out of range. Try again.')



# print(numerical_ranges)

# user_guess = input("Enter a number between 1 and 100: ")
# user_guess = int(user_guess)
# user_guess_decimal = user_guess % 10
# user_guess_str = str(user_guess)

# # print(user_guess) 
# # print(user_guess_decimal)
# # # print(user_guess_decimal)
# # # print(float(user_guess_decimal))

# #if user_guess >= 90 and user_guess_decimal < 5:
# #     print(f'Based on your guess of {user_guess_str}, you scored an A-. Well done!')
# # elif user_guess >= 90 and user_guess_decimal == 5 :
# #       print('Based on your guess of ' + user_guess_str + ', you scored an A. Awesome!')     
# # elif user_guess >= 90 and user_guess_decimal > 5:
# #       print('Based on your guess of ' + user_guess_str + ', you scored an A+. Spectacular!')
# # elif  user_guess >= 80 and user_guess_decimal < 5:  
# #      print('Based on your guess of ' + user_guess_str + ', you scored an B-. Not bad!')
# # elif user_guess >= 80 and user_guess_decimal >= 5:
# #       print('Based on your guess of ' + user_guess_str + ', you scored an B+. Good work!') 
# # else:
# #     print('sorry your score is too low to mention')     



# # elif user_guess >= 80 < 89:
# #     print(f'Based on your guess of {user_guess}, you scored an B. Not too bad my friend!')
# # elif user_guess >= 70 < 79:
# #     print(f'Based on your guess of {user_guess}, you scored an C. Better luck next time my friend!')
# # elif user_guess >= 60 < 69:
# #     print(f'Based on your guess of {user_guess}, you scored an D. Oh dear! do you need help?')
# # else: 
# #     print(f'Based on your guess of {user_guess}, you scored an F. Sorry! See me after this.')


# if user_guess >=90:
#     base_score = 'A'
# elif user_guess >= 80:
#     base_score = 'B'
# elif user_guess >= 70:
#     base_score = 'C'
# else: 
#     base_score = 'O'

# if user_guess_decimal < 5:
#     print(f'Based on your guess of {user_guess_str}, you scored an {base_score}-. Well done!')
# else:
#     print(f'Based on your guess of {user_guess_str}, you scored an {base_score}+. Well done!')