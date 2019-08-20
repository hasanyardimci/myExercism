def is_pangram(sentence):
    p_source = '",.;'
    p_target = '<<<<'
    p_mapping = sentence.maketrans(p_source,p_target)
    myalphabet = "thequickbrownfoxjumpsoverthelazydog"
    sentt = sentence.translate(p_mapping).lower().strip("<")
    if sentt:
        for i in myalphabet:
            if i not in sentt:
                return False
        return True
    else:
        return False