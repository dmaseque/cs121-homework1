import partA as A 
import sys

if __name__ == '__main__':
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    file1_tokens = list(set(A.tokenize(text_file_1)))
    file2_tokens = list(set(A.tokenize(text_file_2)))

    file1_tokens.sort()
    file2_tokens.sort()

    #Algorithm 3: Sorted Lists Approach from Discussion Week 2 slides
    R = []
    file1_index = 0
    file2_index = 0
    while file1_index < len(file1_tokens) and file2_index < len(file2_tokens):
        if file1_tokens[file1_index] < file2_tokens[file2_index]:
            file1_index += 1
        elif file2_tokens[file2_index] < file1_tokens[file1_index]:
            file2_index += 1
        else:
            R.append(file1_tokens[file1_index])
            file1_index += 1
            file2_index += 1
    
    print(len(R))


