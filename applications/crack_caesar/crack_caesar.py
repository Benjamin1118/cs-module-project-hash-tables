# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# add dict with all letter freq

letter_freq = {
    'E'	:11.53,
    'T'	:9.75,
    'A'	:8.46,
    'O'	:8.08,
    'H'	:7.71,
    'N'	:6.73,
    'R'	:6.29,
    'I'	:5.84,
    'S'	:5.56,
    'D'	:4.74,
    'L'	:3.92,
    'W'	:3.08,
    'U'	:2.59,
    'G'	:2.48,
    'F'	:2.42,
    'B'	:2.19,
    'M'	:2.18,
    'Y'	:2.02,
    'C'	:1.58,
    'P'	:1.08,
    'K'	:0.84,
    'V'	:0.59,
    'Q'	:0.17,
    'J'	:0.07,
    'X'	:0.07,
    'Z'	:0.03
}

# Set up needed dictionaries
valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_freq = {}
decode_table = {}
valid_cipher_count = 0
decode = ""

# read in test
with open("ciphertext.txt") as data:
    cipher = data.read()

# count each "char" (letter) in text
for char in cipher:
    if char in valid_char:
        valid_cipher_count += 1
        if char in cipher_freq:
            cipher_freq[char] += 1

        else:
            cipher_freq[char] = 1

# Get the percentage of each letter in the text
for char in cipher_freq:
    freq = round(cipher_freq[char] / valid_cipher_count * 100, 2)

    for letter in letter_freq:
        if letter_freq[letter] == float(freq):
            cipher_freq[char] = freq

# Build a Decode table
for char in letter_freq:
    decode_table[str(letter_freq[char])] = char

# decode the cipher/ text
for char in cipher:
    if char in valid_char:
        key = str(cipher_freq[char])
        decode += decode_table[key]
    else:
        decode += char

# Print result
print(decode)
