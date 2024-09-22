import csv
import pandas as pd

df = pd.read_csv('words3.csv')
words = df['words'].tolist()
letterSet=df['letters'].to_dict()

def wordsByAllLetters(letters):
    possibleWords=[]
    for i in range(len(letterSet)-1):
        if set(words[i]).issubset(letters):
            
            possibleWords.append(words[i])
    returnDict={}
    for i in letters:
        tempList=[]
        for j in possibleWords:
            if j[0]==i:
                tempList.append(j)
        returnDict[i]=tempList
    return returnDict

# def dictWordStartLetter(letters, wordsList):
#     returnDict= {}
#     unusedWords = wordsList
#     for i in letters:
#         tempList=[]
#         for j in unusedWords:
#             if j[0]==i:
#                 tempList.append(j)
#                 unusedWords.remove(j)

        