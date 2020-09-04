# Your code here
ignore = '":;,.-+=/\|[]{}()*^&'
counts = {}
longest = ""

#open and read the file
with open("robin.txt") as f:
    words = f.read().strip().split()
    


def count_word(s):
    for word in words:
        word = word.strip(ignore).lower()
        if word not in counts and word != "":
            counts[word] = 1
        elif word != "":
            counts[word] += 1

def longest_word(words):
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def sort_list():
    sorted_list = list(counts.items())
    sorted_list.sort()

    return sorted_list


def print_histogram(sorted_list, longest_word_len):
    for item in sorted_list:
        hist = " " * (longest_word_len - len(item[0])) + "#" * item[1]
        print(f"{item[0]} {hist}")
    

def run(words):
    count_word(words)
    longest = longest_word(words)
    print_histogram(sort_list(), len(longest))

run(words)



