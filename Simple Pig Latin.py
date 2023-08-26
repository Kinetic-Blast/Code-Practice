import string

def pig_it(text):
    temp,temp2 =text.split(" "),[]
    for i in temp:
        if (i not in string.punctuation):
            temp2.append(i[1:]+i[0]+"ay")
        else: temp2.append(i)
        
    return " ".join(temp2)
