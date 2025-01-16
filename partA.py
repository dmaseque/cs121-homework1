import regex as re
import sys
import os

def tokenize(text_file_path: str) -> list:

    tokens = []

    try:
        with open(text_file_path, 'r', encoding = 'utf-8') as file:
            #use regex to find tokens in each line
            for line in file:
                file_line = re.findall(r'\b[a-zA-Z0-9]+\b', line)
                for token in file_line:
                    tokens.append(token.lower())
    except FileNotFoundError:
        print('File not found.')
    except IOError:
        print('File input/output error.')
    
    return tokens


def compute_word_frequencies(tokens: list) -> dict:

    word_frequencies = {}

    for token in tokens: 
        if token in word_frequencies:
            word_frequencies[token] += 1
        else:
            word_frequencies[token] = 1
    
    return word_frequencies

def print_frequencies(frequencies: dict) -> None:

    sorted_freqs = sorted(frequencies.items(), key = lambda x: (x[0], x[1]), reverse = False)

    for token, frequency in sorted_freqs:
        print(f'{token} = {frequency}')

#test tokenize, compute_word_frequencies, and print_frequencies
if __name__ == '__main__':
    tokens = tokenize(sys.argv[1])
    freqs = compute_word_frequencies(tokens)
    print_frequencies(freqs)

#test the tokenize function
# if __name__ == "__main__":
#     file_path = "example.txt"  # Replace with your text file path
#     token_list = tokenize(file_path)
#     print(token_list)

#test the compute_word_frequencies function
# if __name__ == '__main__':
#     tokens = tokenize(sys.argv[1])
#     freqs = compute_word_frequencies(tokens)
#     print(freqs)