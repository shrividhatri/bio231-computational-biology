'''
Naive Pattern Matching - PYTHON

Implement naive pattern matching for DNA sequences in Python/Perl using for/while loops.
Do NOT use regular expressions.
Text should be read from a file whereas the pattern should be read from standard input.
Your programme should identify all occurrences of the pattern in the text.
'''
retry = 'r'
while(retry == 'r'):
    pattern = input("Enter pattern to search: ")  # input by user

    filename = input("Enter name of text file to search in (e.g. example.txt): ")

    # open file with given filename with read and text flag then read string from it
    text = open(filename,'r').read()
    
    index_found_list = []  # a list storing the integer indexes for the positions in the text string where the pattern matched, initially empty
    times_found = 0  # variable to count the number of times the shorter sequence finds a matching pattern in the longer sequence
    for i in range(len(text)-len(pattern)+1):  # specific range to check indexes so that the pattern is not checked out of bounds in the text string
        text_substr = text[i:len(pattern)+i]  # substring of text of same length as pattern starting from index i
        if pattern == text_substr:  # if the pattern matches the text substring, increment the counter times_found
            times_found += 1
            index_found_list.append(i)  # and add the current index where it matched to the index_found_list by appending

    print("The pattern %s was found %i times in the text %s by naive pattern matching at indexes:" % (pattern, times_found, text), index_found_list)
    retry = input('Enter \'r\' to do another search, any other key to terminate the program: ') # retry input
    print('\n')
