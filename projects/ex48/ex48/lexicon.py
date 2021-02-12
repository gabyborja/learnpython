def scan(user_input):
    """Scan user input for words that fit in lexicon
    1. Break up sentence
    2. Scan words for their type
    3. Return tuple
    4. Make sentence out of them """
    print("lexicon Scan function")
    print(f"{user_input}")

    words = user_input.split()
    print(f"words {words}")
    print(f"length of list {len(words)}")
    sentence = []
    

    for i in words:
        print(i)
        if i in ['north', 'south', 'east']: #check if word belongs to lexicon
            sentence.append(('direction', i))# return tuple 
            print(f'in lexicon {i}')
            print(f'return {sentence}')
        else:
            sentence[i] = ('error', words(i))
    
    return sentence
   # return sentence