import random

# run, right, fast
# uper
## Understand 

## Plan - done if good psudocode...
# read input.txt and split to words
#read in.
#split to words


#analyze text build ds of words
# words that can follow a word? word that actually does
# any word at index +1
#how 2 build dataset

# use a hashtable
# good way to relate one piece of in infor with other info, relational
# frequent lookups
#key : word, value: list of all wordd that can follow this word

# choose a random start word to begin
#What is a start word
# first or second char is capitalized

#make list of start words

# loop through and choose rand following word if a stop word stop
#stop words ends with .?!, or second to last char is


##

# Read in all the words in one go
with open('input.txt') as f:  #"applications/markov/input.txt") as f:
    words = f.read()

split_words = words.split()


# TODO: analyze which words can follow other words
# Your code here
ds = {}

for i in range(len(split_words) -1):
    word = split_words[i]
    next_word = split_words[i+1]

    if word not in ds:
        ds[word] = [next_word]

    else:
        ds[word].append(next_word)

#make a list of start words
## first/ second char is capitalized
## Loop over split words and put any start words into list

# add a .keys() method to hashtable class
start_words = []
for key in ds.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)


# TODO: construct 5 random sentences
# Your code here

stopped = False
stopped_signs = '.!?'

while not stopped:
    # print the word
    print(word, end= ' ')

    ##if it's a stop word stop
    if word[-1] in stopped_signs or len(word) >1 and word[-2] in stopped_signs:
        stopped = True
    #choose a random following word
    following_words = ds[word]

    word = random.choice(following_words)

