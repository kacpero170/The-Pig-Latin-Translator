# This is a simple Pig Latin Translator

# Pig Limitations
app1 = 'yay'
app2 = 'ay'
vowels = ['a','e','i','o','u']

# Variables
word = input('Enter your word: ')
first = word[0]
rest = word[1:]
new_first = rest[0].upper()
new_rest = rest[1:].lower()

# Translator
if (len(word) > 0) and (word.isalpha()) and (first.lower() in vowels):
    print(first.upper() + rest.lower() + app1)
elif (len(word) > 0) and (word.isalpha()) and (first.lower() not in vowels):
    def move_letters_to_end(word):
        for index, letter in enumerate(word):
          if letter.lower() in vowels:
            return word[index:] + word[:index]
        return word
    result = move_letters_to_end(word)
    result_first = result[0].upper()
    result_rest = result[1:].lower()
    print(result_first + result_rest + app2)
else:
    print('Your word may contain numbers. Choose a different word and try again.')