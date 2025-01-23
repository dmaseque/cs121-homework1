import partA as A 
import sys

if __name__ == '__main__':
    text_file_1 = sys.argv[1]
    text_file_2 = sys.argv[2]

    file1_tokens = A.tokenize(text_file_1)
    file2_tokens = A.tokenize(text_file_2)

    file1_tokens.sort()
    file2_tokens.sort()

    #Algorithm 3: Sorted Lists Approach from Discussion Week 2 slides
    R = []
    file1_iter = iter(file1_tokens)
    file2_iter = iter(file2_tokens)
    try:
        file1_val = next(file1_iter)
        file2_val = next(file2_iter)
        while True:
            if file1_val < file2_val:
                file1_val = next(file1_iter)
            elif file2_val < file1_val:
                file2_val = next(file2_iter)
            else:
                R.append(file1_val)
                file1_val = next(file1_iter)
                file2_val = next(file2_iter)
    except StopIteration:
        pass
    
    
    print(len(set(R)))


