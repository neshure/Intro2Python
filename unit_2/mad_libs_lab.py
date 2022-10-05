"""
- using input function........
- prints the prompt message and wait for the user to hit Enter
- Once the user types in their entry and hit Enter, 
- python returns their input with formatted statement
 """



exclamation = input("Enter exclamation: ")
adverb = input("Enter adverb: ")
noun = input("Enter noun: ")
adjective = input("adjective: ")

game = f'''
"This is a Mad Libs Game. Hope you like it"
------------------------------------------
exclamation ---- {exclamation}
adverb -------- {adverb}
noun --------- {noun}
adjective ------- {adjective}
'''
print(game)

sentence = f'"{exclamation}" he sreamed {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife'

print(sentence)
