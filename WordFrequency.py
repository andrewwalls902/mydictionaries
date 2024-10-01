import string

def count_word_frequencies(filename):
    
    with open('sometext-1.txt', 'r') as file:
        sometext= file.read().lower()  

   
    sometext = sometext.translate(str.maketrans('', '', string.punctuation))


    words = sometext.split()

    word_frequencies = {}

    
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    # Display the frequency of each word
    for word, frequency in word_frequencies.items():
        print(f"'{word}': {frequency}")


count_word_frequencies('sometext-1.txt')
