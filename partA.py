import regex as re
import sys
import os

# Time Complexity: O(n), where n is the total number of characters
# Open file and check if file is empty is O(1). Outer for loop reading each line of file and regular
# expression statement is O(n). Inner for loop iterating for each token in that file line is O(n).
# Exception handling is O(1). 
# O(1) + O(n) + O(n) + O(1) = O(n) 
def tokenize(text_file_path: str) -> list:

    tokens = []

    try:
        #open the file and read
        with open(text_file_path, 'r', encoding = 'utf-8') as file:
            #check if the file is empty w/o reading entire file
            if file.read(1):
                file.seek(0)
                #use regex to find tokens in each line
                for line in file:
                    file_line = re.findall(r'[a-zA-Z0-9]+', line)
                    for token in file_line:
                        tokens.append(token.lower())
            else:
                print("File is empty.")
    except FileNotFoundError:
        print('File not found.')
    except IOError:
        print('File input/output error.')
    
    return tokens

# Time Complexity: O(n), where n is the total number of tokens in tokens list
# For loop iterates through every token in tokens list = O(n)
# If statements to check if token already exists in word_frequencies (hash/map) = O(1)
# n * O(1) = O(n)
def computeWordFrequencies(tokens: list) -> dict:

    word_frequencies = {}

    for token in tokens: 
        if token in word_frequencies:
            word_frequencies[token] += 1
        else:
            word_frequencies[token] = 1
    
    return word_frequencies

# Time Complexity: O(nlogn), where n is total number of token, frequency pairs in frequencies dict
# To sort frequencies dict, sorted function = O(nlogn)
# For loop iterates through every token, frequency pair in frequencies dict = O(n)
def print_frequencies(frequencies: dict) -> None:

    sorted_freqs = sorted(frequencies.items(), key = lambda x: (-[1], x[0]))

    for token, frequency in sorted_freqs:
        print(f'{token} - {frequency}')

#test tokenize, compute_word_frequencies, and print_frequencies
if __name__ == '__main__':
    tokens = tokenize(sys.argv[1])
    freqs = computeWordFrequencies(tokens)
    print_frequencies(freqs)

#test the tokenize function
# if __name__ == "__main__":
#     file_path = "example.txt"  # Replace with your text file path
#     token_list = tokenize(file_path)
#     print(token_list)

#test the compute_word_frequencies function
# if __name__ == '__main__':
#     tokens = tokenize(sys.argv[1])
#     freqs = computeWordFrequencies(tokens)
#     print(freqs)