str = input("Enter a Char: ")
vowel = str.strip().lower()
if vowel in 'aeiou':
    print(f"'{vowel}' is a vowel.")
else:
    print(f"'{vowel}' is not a vowel.")