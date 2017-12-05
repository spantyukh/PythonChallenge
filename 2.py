# -*- coding: utf-8 -*-

def rename(t):
    i = 0
    a1 = "ёйцукенгшщзхфвапролджэячсмитбю"
    A1 = "ЁЙЦУКЕНГШЩЗХФВАПРОЛДЖЭЯЧСМИТБЮ"
    while i < len(a1):
        if t[0] == a1[i]:
            t1 = A1[i] + t[1:]
        elif t[0] == A1[i]:
            t1 = A1[i] + t[1:]
        i = i+1
    return(t1)

textOpen = open("text.txt", 'r', encoding='utf-8')
outTextOpen = open("result.txt", 'w', encoding='utf-8')
Text = textOpen.read()
tempWords=Text.split()
outText = ""
i = 0
while i < len(tempWords):
    if len(tempWords[i]) > 6:
        tempWords[i] = rename(tempWords[i])
    outText = outText + tempWords[i] + " "
    i = i+1
outTextOpen.write(outText)
outTextOpen.close()
textOpen.close()
