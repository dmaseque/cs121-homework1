import partA as A 
import sys

# Time Complexity: O(nlogn), where n is the total number of characters
# Tokenize text_file_1 and text_file_2 = O(n) + O(m), where n is the total number of characters of the smaller text file
# and m is the total number of characters of the larger text file
# Sort text_file_1 and sort text_file_2 = O(nlogn) + O(mlogm)
# While loop iterates through the file1_tokens and file2_tokens = O(n), where n is the total number of characters of smaller text file
# O(n) + O(m) + O(nlogn) + O(mlogm) + O(n) = O(nlogn)
if __name__ == '__main__':

    #take two text files from the command line as arguments
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    #tokenize text_file_1 and text_file_2, use set to remove any duplicates
    file1_tokens = list(set(A.tokenize(text_file_1)))
    file2_tokens = list(set(A.tokenize(text_file_2)))

    #sort the tokens by alphabetical order
    file1_tokens.sort()
    file2_tokens.sort()

    #Algorithm 3: Sorted Lists Approach from Discussion Week 2 slides
    R = []
    file1_index = 0
    file2_index = 0
    #iterate through both text files, stop when reached end of one of the files
    while file1_index < len(file1_tokens) and file2_index < len(file2_tokens):
        #if file_1 value < file2_value, increment file1_index
        if file1_tokens[file1_index] < file2_tokens[file2_index]:
            file1_index += 1
        #if file_2 value < file1_value, increment file2_index
        elif file2_tokens[file2_index] < file1_tokens[file1_index]:
            file2_index += 1
        #if file1_value = file2_value, append to R and increment both indexes
        else:
            R.append(file1_tokens[file1_index])
            file1_index += 1
            file2_index += 1
    
    #print length of R = how many number of tokens text_file_1 and text_file_2 have in common
    print(len(R))


