import re

def count_words(sentence):
    sentence = sentence.lower()
    words_list = re.findall(r"[a-z']+|[0-9]+", sentence)
    
    words = {}
    for word in words_list:
        word = word.strip("'")
        if not word:
            continue
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    return words

        
        
