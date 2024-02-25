def is_vowel(char):
    char = char.lower()
    
    if char in ['a','e','i','o','u']:
        return True
    else:
        return False
    

print(is_vowel('a','b'))

print(is_vowel('p'))