import numpy as np

testLetters = set(("h","r","w","m","c","a","t","o","f","e","l","n","s"))
testMap = [["h", "r", "w", "m"],["c","a","t","o"],["f","e","t","l"],["h","n","l","s"]]
testWords = {"h":["hate", "hat", "hen"]}

grid = [[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(2,1),(3,1)],[(0,2),(1,2),(2,2),(3,2)],[(0,3),(1,3),(2,3),(3,3)]]

class Path:
    def __init__(self, coord,map, words, usedSpaces:list, letters, grid, count):
        self.coord = coord
        self.map = map
        self.words = words
        self.myLetter = self.coordToLetter(self.coord, self.map)
        self.word = letters+self.myLetter
        self.usedSpaces = self.addUsedSpace(self.coord, usedSpaces)
        self.grid = grid
        self.frontier = self.getFrontier(self.coord, self.grid, self.usedSpaces)
        self.newWords = []
        self.count=count+1

    def coordToLetter(ctl, coord, map):
        x=coord[0]
        y=coord[1]
        #print(x,y)
        #print(map)
        ctl.letter = map[y][x]
        return ctl.letter
    
    def addUsedSpace (aus, coord, usedSpaces):
        aus.usedSpaces = list(usedSpaces)
        aus.usedSpaces.append(coord)
        return aus.usedSpaces


    def getFrontier(gF, coord, grid, usedSpaces):
        gF.usedSpaces = usedSpaces
        gF.coord = coord
        gF.grid = grid
        gF.frontier = []

        top = 0
        bottom = 0
        right =0
        left = 0
        if gF.coord[0] == 0:
            left = 0
            right = 1
        elif gF.coord[0] == 3:
            left = 2
            right = 3
        else:
            left = gF.coord[0] - 1
            right = gF.coord[0] +1

        if gF.coord[1] == 0:
            top = 0
            bottom = 1
        elif gF.coord[1] == 3:
            top = 2
            bottom = 3
        else:
            top = gF.coord[1] - 1
            bottom = gF.coord[1] +1
        
        #print((top,bottom),(left,right))

        for i in range(top,bottom+1):
            for j in range(left, right+1):
                if (j,i) not in gF.usedSpaces:
                    gF.frontier.append((j,i))
                # else:
                #     print(usedSpaces, coord in usedSpaces, (j,i))
        # print(gF.frontier)
        return gF.frontier
    
    def walkPath (wP, frontier:list, coord, map, usedSpaces, grid, count,word, words):
        newWords = []
        frontier = frontier
        # print(word, coord)
        # print(frontier)
        if word in words:
            newWords.append(word)
        
        
        
        if count == 8:
            return newWords
        elif len(frontier)==0:
            return newWords
        else:
            for i in frontier:
                child=Path(i, map, words, usedSpaces, word, grid, count)
                childNewWords = child.walkPath(child.frontier, child.coord, child.map, child. usedSpaces, child.grid, child.count, child.word, child.words)
                #print(childNewWords)
                if childNewWords != []:
                    for j in childNewWords:
                        if j not in newWords:
                        
                            newWords.append(j)
            return newWords

        
    
# shimy = Path((0,0),testMap, testWords["h"], [(1,0),(0,1),(2,0)], "",grid,0)
# print(shimy.walkPath(shimy.frontier, shimy.coord, shimy.map, shimy.usedSpaces, shimy.grid, shimy.count, shimy.word, shimy.words))
    

