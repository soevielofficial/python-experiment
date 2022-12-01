# Exercise 1

vowels = set('aiueo')
word = input("Enter a word to search for vowels:    ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)

# The code above is the code used to search for letters vowel based on the input word. The code has not been wrapped to in a function. To wrap the code in a function, add the following code:

def search4vowels():
    vowels = set('aiueo')
    word = input("Enter a word to search for vowels:    ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels() # We wrapped the previous code snippet into a function with a name "search4vowels()". Run the code.

# Exercise 2

def search4vowels(word):
    """Displays vowels based on the word entered"""
    vowels = set('aiueo')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

# The code above is a function with one argument, if we If you do not enter an argument in the function, an error will appear TypeError: search4vowels() missing 1 required positional argument: 'word' this error is caused because of the search4vowels() function takes one argument.

# Exercise 3

def search4vowels(word):
    """Displays vowels based on the word entered"""
    vowels = set('aiueo')
    found = vowels.intersection(set(word))
    return bool(found)

# In the function above we replace the output of the previous function using a for loop to return bool(found) which later the output will display True or False according to arguments entered.

# Exercise 4

def search4vowels(word):
    """Displays vowels based on the word entered"""
    vowels = set('aiueo')
    found = vowels.intersection(set(word))
    return found

# In the function above we replace the output of the function that was previously using boolean to be output according to the vowel found use returnfound.

# Exercise 5

def search4vowels(word:str) -> set:
    """Displays vowels based on the word entered"""
    vowels = set('aiueo')
    found = vowels.intersection(set(word))
    return found

# In the above function we explicitly add data types to the arguments and output that will be displayed later. The argument is a string data type and the output is a data set type.

# Exercise 6

def search4letter(phrase:str, letter:str) -> set:
    """Returns a value in set form based on the letter found in the phrase"""
    return set(letter).intersection(set(phrase))

# In the above code we create a function to display the letters found in a phrase

# Exercise 7

def search4letter(phrase:str, letter:str='aiueo') -> set:
    """Returns a value in set form based on the letter found in the phrase"""
    return set(letter).intersection(set(phrase))

# In the code above we add a default value to the argument letters