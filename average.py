import text_utils                                                   # Imports the code that counts the number of characters, words, and sentences.

def line_count():
    
    file = open('sample.txt', 'r')                                  # Opens the file in read-only mode.

    lines = len(file.readlines())                                   # Counts the number of lines in the file.

    file.seek(0)                                                    # Goes back to the start of the file, so it can be reread.

    word_total = text_utils.count_words(file.read())                # Rereads the file to count how many words there are.
    
    file.close()                                                    # Closes the file.

    average = word_total // lines                                   # Divided the number of words by the number of lines, and rounds down.

    return (f"Average words per line: {average}")                   # Returns the average words per line.

line_count()
lc = line_count()
print(lc)                                                           # Prints the line_count function.