vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)


"""The final version of the vowels
program, “vowels7.py", took
advantage of Python’s set data
structure to considerably shrink
the list-based “vowels3.py” code,
while still providing the same
functionality"""