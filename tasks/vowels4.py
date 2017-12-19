vowels = [ 'a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k,'was found',v, 'time(s).')


"""This is the code for
“vowels4.py”, which
performed a frequency
count. This code was
(loosely) based on
“vowels3.py”, which we
first saw in Chapter 2."""