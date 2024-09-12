def count_chars(text):

    char_total = len(text)                                                  # Counts how many characters there are in the text.

    return char_total                                                       # Returns the total number of characters that are in the text.
    
def count_words(text):                                                      

    word_total = len(text.split())                                          # Splits the words into separate strings and counts the number of strings.

    return word_total                                                       # Returns the total number of words that are in the text.

def count_sentences(text):
    
    sen_total = text.count(".") + text.count("!") + text.count("?")         # Counts how many sentence ending puncuation marks there are in the text.
    
    return sen_total                                                        # Returns the number of sentences based on how many sentence ending puncuation marks there are.