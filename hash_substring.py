# python3

# From lecture 8 - Hashing
B = 13  # coefficient for formula  H = sum(c(n) * b^m-n) or productOf(c(n) + b)


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    pattern = ""
    string = ""

    if "F" in text:
        file_name = input()
        file = open(file_name, "r")
        # file = open("./tests/06", "r")
        text = file.read()
        # after input type choice
        # read two lines
        text = text.split('\n')
        pattern = text[0]
        string = text[1]

    elif "I" in text:
        # first line is pattern
        # second line is text in which to look for pattern
        pattern = input()
        string = input()

    # return both lines in one return
    # this is the sample return, notice the rstrip function
    pattern = pattern.strip()
    string = string.strip()
    print("'", pattern, "'")
    print("'", string, "'")
    return (pattern, string)


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    pattern_length = len(pattern)
    text_length = len(text)

    pattern_hash = get_hash(pattern)
    occurrence = []

    sub_string = text[:pattern_length]  # substring will be first chars (as many as in pattern) of text
    index_for_end_char = pattern_length - 1
    for i in range(text_length - pattern_length + 1):
        sub_string_hash = get_hash(sub_string)
        print(sub_string)
        print(i)
        print(pattern_hash)
        print(sub_string_hash)
        if sub_string_hash == pattern_hash:

            if sub_string == pattern:
                occurrence.append(i)
        if index_for_end_char < text_length - 1:
            index_for_end_char = index_for_end_char + 1
            sub_string = sub_string[1:]  # Remove first char from pattern
            sub_string = sub_string + text[index_for_end_char]  # Add new char to search patter to end

    # and return an iterable variable
    return occurrence


def get_hash(pattern):
    m = len(pattern)
    # my_hash = 1 # product
    my_hash = 0  # sum
    for i in range(m):
        # my_hash = my_hash * (ord(pattern[i]) + B) # product
        my_hash = my_hash + ord(pattern[i]) * pow(B, m - i)  # sum
    return my_hash


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
