def rep_split_word(words):
    return words.replace('-',' ').replace('_',' ').upper().split()

def abbreviate(words):
    r = ""
    w = rep_split_word(words)
    print (w)
    for i in range(len(w)):
        r += w[i][0]
    return r
