def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename,search):
    """Count the approximate number of times word appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        search = search.lower()
        words = contents.count(search)
        print(f"The word, {search}, occurred {words} times in the {filename} file")

filenames = ['cookingdirty.txt', 'dangerousgames.txt', 'theageofwonder.txt']
for filename in filenames:
    count_words(filename)

s = input("What common word would you like to search for within the files?: ")
for filename in filenames:
    find_words(filename,s)