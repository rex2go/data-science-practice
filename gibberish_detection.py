import numpy as np

# markov example #1

# remove line breaks and spaces from text
'''file = open('text.txt', 'r')
data = file.read().replace('\n', '').replace(' ', '').lower()
file.close()

file = open('text1.txt', 'wt')
file.write(data)
file.close()'''

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ'.lower() # define char set
nested = dict() # create dict for nested chars
file = open('text1.txt', 'r') # load up data
data = file.read()

# fill nested with charset
for char in charset:
    occurences = dict()

    for nested_char in charset:
        occurences[nested_char] = 0

    nested[char] = occurences

# sum up occurences of the following character
for index, char in enumerate(data):
    if index+1 != len(data):
        if char in nested and data[index+1] in nested:
            nested[char][data[index+1]] = nested[char][data[index+1]] + 1

# absolute occurences to percent
for char in nested:
    sum = 0

    for nested_char in nested[char]:
        sum = sum + nested[char][nested_char]

    for nested_char in nested[char]:
        nested[char][nested_char] =  nested[char][nested_char] / sum

# get input
inp = input('Input: ').lower()
p = 0

for index, char in enumerate(inp):
    if index+1 != len(inp):
        if char in nested and inp[index+1] in nested:
            p = p + nested[char][inp[index+1]]

p = p / len(inp)
pc = str(round(p * 100)) + '%'

if p < 0.06:
    print('Gibberish ' + pc)
else:
    print('No Gibberish ' + pc)
