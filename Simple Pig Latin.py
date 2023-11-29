"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""


import string

def pig_it(text):
    temp,temp2 =text.split(" "),[]
    for i in temp:
        if (i not in string.punctuation):
            temp2.append(i[1:]+i[0]+"ay")
        else: temp2.append(i)
        
    return " ".join(temp2)
