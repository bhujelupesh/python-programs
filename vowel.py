vowel = ['a','e','i','o','u']

letter = input("Enter the letter to check: ")
letter = letter.lower()
if letter in vowel:
    print("Vowel")
else:
    print("Not vowel")