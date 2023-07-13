"""
Input: 
This is an example for this example

Output:
This=1
is=1
an=1
example=2
for=1
this=1
"""

# 1. Get a text input from a user
# Eg:"To find out the  type of a value or a variable that refers to that value, you can use the type function"
# w = input("Enter user input:")

# f = open('text_file.txt', 'r', encoding='utf8')
# w= f.read()
# f.close()
with open('text_file.txt', 'r', encoding='utf8') as f:
    w = f.read()
    print(f"File Content: \n{w}\n")

# 2. Break words at blank spaces and save in 'words' variable ['To', 'find', 'out', ... 'function']
words = w.split()

# remove common words from text_file.txt
stop_words = {'the', 'to', 'for', 'a'}

# iterate over the words
for wd in words:
# check if the word is in stop_words
    if wd in stop_words:
        words.remove(wd)


# 3. Create a dictionary named counter
counter={}

# 4. Iterate the words variable and add to counter dictionary {"To": 1, "out": 1, "function":1}
# counter['key'] = value, eg: counter['random word'] = 1
for w in words:     # ['To', 'find', 'out', ... 'function']

    # 4.1 If a new  word is found add to dictionaty with value 1
    if  w not in counter:
        # Add to dict and assign value as 1
        counter[w] =1

    # 4.2 If word is repeated, increment by 1 from its previous value
    elif w in counter:
        # use the previous value and increment by 1
        counter[w] = counter[w] + 1     # counter[w] += 1

# 5. Format the counter to look like our expected output
print("Frequency count:", counter)
