def convert_number(s): 
    try:
        return int(s)
    except ValueError:
        return None

def scan(user_input):
    """Scan user input for words that fit in lexicon
    1. Break up sentence
    2. Scan words for their type
    3. Return tuple
    4. Make sentence out of them """
    #print("lexicon Scan function")
    #print(f"{user_input}")

    words = user_input.split()
    #print(f"words {words}")
    #print(f"length of list {len(words)}")
    sentence = []
    

    for word in words:
        word_check = word.lower() # Making sure to handle capitalization
        #print(word_check)
        if word_check in ['north', 'south', 'east']: # direction lexicon
            sentence.append(('direction', word))
            #print(f'in direction lexicon {word}')
            #print(f'return {sentence}')
        elif word_check in ['go', 'stop', 'kill', 'eat']: # verb lexicon
            sentence.append(('verb', word))
            #print(f'in verb lexicon {word}')
            #print(f'return {sentence}')
        elif word_check in ['the', 'in', 'of', 'from', 'at', 'it']: # stop lexicon
            sentence.append(('stop', word))
            #print(f'in stop lexicon {word}')
            #print(f'return {sentence}')
        elif word_check in ['door', 'bear', 'princess', 'cabinet']: # noun lexicon
            sentence.append(('noun', word))
            #print(f'in noun lexicon {word}')
            #print(f'return {sentence}')
        else:
            number = convert_number(word)
            #print(f"word_int {number}")
            if number != None: 
                sentence.append(('number', number))
            else:
                sentence.append(('error', word))

    return sentence