"""
Objectives:
- Lists
- Dict
- constructs: loops, conditionals
- more work with files
- functions
"""

# function #1
"""
    Returns the number of lines in a file given as parameter.
    @param filename: the file's name
"""
def numlines(filename):
    count = 0
    with open(filename, 'r') as input_file:
        for line in input_file:
            count = count + 1
    return count

# function #2
"""
    Reads the content of a file and fills the given list with the sentences
    found in the file
    @param filename: the file's name
    @param sentences: the list that will be contain the sentences
"""

def get_sentences(filename, sentences):
    with open(filename, 'r') as input_file:
        str = input_file.read()
    sentences += str.split(". ")

# function #3
"""
    Return a list of the top N most used words in a given file
    @param filename: the file's name
    @param n: the number of words in the top, default is 5
"""
def most_used(filename, n=5):
    with open(filename, 'r') as input_file:
        str = input_file.read()
        words = str.split()
        mp = {}
        for w in words:
            if w not in mp:
                mp[w] = 1
            else:
                mp[w] += 1
    return sorted(mp, key = mp.get, reverse=True) [0:n]

if __name__ == "__main__":

    filename = "fisier_input"

    result1 = numlines(filename)
    print(result1)

    sentences = []
    get_sentences(filename, sentences)
    print(sentences)

    result2 = most_used(filename, 10)
    print(result2)