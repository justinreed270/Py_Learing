def search(word, text):
    """Return tuple holding line num and line text (or None)."""
    for line in enumerate(text, 1):
        if line[1].find(word) >= 0:
            return line
    return None


def main():
    with open('zen_of_python.txt') as f:# Open my_files/zen_of_python.txt and
        zop = f.readline() #create a list from its contents
         # Save the list as zop

    word = input('Enter search word: ')
    result = search(word, zop)
    if result:
        print(word, ' first appears on line ',
              result[0], ': ', result[1], sep='')
    else:
        print(word, 'was not found.')

main()
