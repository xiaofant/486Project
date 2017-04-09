# -*- coding: utf-8 -*-
import preprocessor as p
import sys
import re

def isDate(s):
    if re.match(r'\w+/\d{2}/\d{4}|\w+-\d{2}-\d{4}', s):
        return True
    return False

def preprocess(tweet):
    p.set_options(p.OPT.URL, p.OPT.EMOJI)
    clean = p.clean(tweet)
    clean = clean.replace("#","")

    # copy of tokenizer from my previous project
    # using http://grammar.about.com/od/words/a/EnglishContractions.html for reference of contractions
    cont = open("Contractions in English")
    line = cont.readline()
    contractions = {}

    while line:
        line = line.strip()
        line = re.split('\s+', line)
        contraction = line[0]
        expand = ""
        for i in range(1, len(line)):
            expand += line[i] + " "
        contractions[contraction] = expand[:-1]
        line = cont.readline()

    input = clean.lower()
    input = input.strip()
    input = re.split('\s+', input)

    output = []

    for i in range(0, len(input)):
        word = input[i]
        # remove all other symbols/characters that are not mentioned
        word = re.sub("[^a-z0-9-.'/,]", '', word).strip()
        if word in contractions:
            match = contractions[word]
            output.extend(re.split('\s+', match))
        elif len(word) > 2 and (word[-2:] == "'s" or word[-2:] == "s'"):
            # handle possessive
            output.append(word[:-2])
            output.append("'s")
        elif isDate(word):
            output.append(word.strip())
        elif re.match(r'\w*,\w*', word):
            # tokenization of ,
            if re.match('\d+,\d+', word):
                # case of number
                output.append(word)
            else:
                word = re.sub(',', '', word).strip()
                if word != "":
                    output.append(word)
        elif re.match(r'\w*\.\w*', word):
            # tokenization of .
            if word == ".":
                continue
            elif re.match(r'\w{2,}\.', word) and word != "mr." and word != "dr." and word != "st." \
                    and word != "oz." and word != "ms." and word != "jr." and word != "sr." and \
                            word != "mt." and word != "no." and word != "sq.":
                # some popular two-characters abbreviations from http://www.englishleap.com/other-resources/abbreviations
                output.append(word[:-1])
            else:
                # take else and all one char ended with a '.' as abbreviations/acronyms
                output.append(word.strip())
        else:
            word = re.sub("[^a-z0-9-.]", ' ', word).strip()
            if word == '':
                continue
            output.append(word)

    return output