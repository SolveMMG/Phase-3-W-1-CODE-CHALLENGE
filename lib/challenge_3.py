# Defining function
def solve(word):
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    # Creating variable to store vowels
    vowels = "aeiou"

    # Variables to store max value and current value
    highest_consonant_value = 0
    consonant_current_value = 0

    # Looping through the word characters.
    for char in word:
        # Checking if its a vowel
        if char not in vowels:
            # Adding consonant values
            consonant_current_value += consonant_values[char]
        # Runs when a vowel is encountered
        else:
            # Setting max value
            highest_consonant_value = max(highest_consonant_value, consonant_current_value)
            # Reseting current consonant value
            consonant_current_value = 0

    # Returning max consonant value
    return highest_consonant_value

