#strings in python
sentence = '''strings in python'''
print(sentence[8]) # accessing one element
print(len(sentence)) # length of the string
print(sentence[5:9]) # slicing
print(sentence[11:])
print(sentence[:5])
print(sentence.split(" ")) #spliting
for letter in sentence: #accessing each element
    print(letter)