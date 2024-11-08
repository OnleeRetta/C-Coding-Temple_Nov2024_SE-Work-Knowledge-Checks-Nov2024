# Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Convert number to string
def number_to_string(number):
    # Convert the integer to a string
    return str(number)

# Vowel Count
def get_count(sentence):
    count_vowels = 0
    for vowels in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += sentence.count(vowels)
    return count_vowels