import partA as A 
import sys

# Time Complexity: O(nlogn), where n is the total number of characters
# Tokenize text_file_1 and text_file_2 = O(n) + O(m), where n is the total number of characters of the smaller text file
# and m is the total number of characters of the larger text file
# Sort text_file_1 and sort text_file_2 = O(nlogn) + O(mlogm)
# While loop iterates through the file1_tokens and file2_tokens = O(n), where n is the total number of characters of smaller text file
# O(n) + O(m) + O(nlogn) + O(mlogm) + O(n) = O(nlogn)
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


