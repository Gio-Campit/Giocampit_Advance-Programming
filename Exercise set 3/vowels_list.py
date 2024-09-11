def find_vowels (input_string):
    vowels = "a, e, i, o, u, A, E, I, O, U"
    vowels =[char for char in input_string if char in vowels]
    print(vowels)

input_string = input("Enter a word: ")
find_vowels(input_string)