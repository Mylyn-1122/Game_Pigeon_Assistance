import dataAccess
import pathFinder

#get the rows
rows=[]
while True:
    allLetters = input("please imput all letters: ")
    if len(allLetters)==16:
        for i in range(0,15,4):
            tempList = list(allLetters[i:i+4])
            rows.append(tempList)
        break
    else:
        print("please type in 16 letters")
        continue


presentLetters=set(allLetters)


allWords=dataAccess.wordsByAllLetters(presentLetters)

grid = [[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(2,1),(3,1)],[(0,2),(1,2),(2,2),(3,2)],[(0,3),(1,3),(2,3),(3,3)]]
#print(rows)

newWords = []

for i in range(0,4):
    for j in range(0,4):
        coord = (j,i)
        letter = rows[i][j]
        path = pathFinder.Path(coord, rows, allWords[letter], [], "", grid, 0)
        pathResult= path.walkPath(path.frontier, path.coord, path.map, path.usedSpaces, path.grid, path.count, path.word, path.words)
        for k in pathResult:
            if k not in newWords:
                newWords.append(k)
        

# path = pathFinder.Path((0,0), rows, allWords["h"], [], "", grid, 0)
# pathResult= path.walkPath(path.frontier, path.coord, path.map, path.usedSpaces, path.grid, path.count, path.word, path.words)

# print(pathResult)
print(sorted(newWords, key=lambda l: (len(l),l)))
#print(newWords)
