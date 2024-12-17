def numberOfWords(text):
    number = len(text.split())
    return number

def numberOfCharacters(text):
    letterDict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for letter in text:
        for character in letterDict:
            if letter == character:
                letterDict[character] += 1

    sortedDict = sorted(letterDict.items(), key=lambda x:x[1], reverse=True)

    return sortedDict

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    totalWords = numberOfWords(text)

    print(totalWords, "words found in the document")
    print()

    totalCharacters = numberOfCharacters(text)

    for key, value in totalCharacters:
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report(file_contents)

main()
