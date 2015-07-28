#cfg = Context-free grammar
#https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
#This should be the guide to the tagset.

import nltk
import en

def rearrange(sent):
    for w in sent:
        #This should check for all punctuation, and make it simpler.
        if w[1] in "$'(),--.:SYM":
            w = (w[0],'.')
    temp_sentence = []
    temp_adjectives = []
    for w in sent:
        #Adjectives and adverbs
        s = str(w)
        slist = s.split("'")
        typ = slist[3]
        #adjectives.
        if typ in 'CDJJRJJSRBR':
            temp_adjectives.append(w)
        elif typ in 'CC.':
            if temp_adjectives:
                temp_adjectives.append(w)
            else:
                temp_sentence.append(w)
        else:
            temp_sentence.append(w)
            for i in temp_adjectives:
                temp_sentence.append(i)
            temp_adjectives = []
    sent = temp_sentence
    return sent

def convert(text1):
    sentence_1 = []
    sentence = nltk.pos_tag(nltk.word_tokenize(text1))
    for i in sentence:
        sentence_1.append(( str(i[0]), str(i[1]) ))
    sentence_1 = rearrange(sentence_1)
    string = ''
    for w in sentence_1:
        if string and w[1] != '.':
            string += ' '
        string += w[0]
    
    print string


started = 0
text = raw_input('')
while (text != ' '):
    if started:
        if text[0] != '_':
            temp = ''
            temp_list = []
            temp_list = text.split(' ')
            lazy = 0
            for x in temp_list:
                try:
                    x = int(x)
                except:
                    pass
                if lazy == 0:
                    temp += en.number.spoken(x)
                    lazy = 1
                else:
                    temp += ' ' + en.number.spoken(x)
            text = temp
            convert(text)
        else:
            print text
    else:
        print text
        if text == '***':
            started = 1
    text = raw_input()
print en.is_number("twelve")
print en.is_basic_emotion("cheerful")











