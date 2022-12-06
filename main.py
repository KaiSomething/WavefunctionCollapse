from random import randint
from math import copysign

class Position:
    def __init__(self, variants):
        self.state = variants
    def collapse(self):
        if(type(self.state) is list):
            self.state = self.state[randint(0, len(self.state)-1)]

class Board:
    def __init__(self, width, height, rules, isTile=False):
        self.icons = None
        self.width = width
        self.height = height
        self.isTile = isTile
        self.rules = rules
        self.board_list = []
        for y in range(self.height):
            self.board_list.append([])
            for x in range(self.width):
                self.board_list[y].append(Position(self.rules.variants))
    def setIcons(self, icons):
        self.icons = icons
    def __str__(self):
        s = ""
        for y in range(self.height+2):
            for x in range(self.width+2):
                if((y == self.height+1 and x == self.width+1) or 
                  (y == 0 and x == self.width+1)):
                    s += "+"
                elif((y == self.height+1 and x == 0) or 
                  (y == 0 and x == 0)):
                    s += "+-"
                elif(y == self.height+1 or y == 0):
                    s += "--"
                elif(x == 0):
                    s += "| "
                elif(x == self.width+1):
                    s += " |"
                else:
                    if(type(self.board_list[y-1][x-1].state) is list):
                        s += "~"
                        #s += str(self.board_list[y][x].state) + " "
                    else:
                        if(not self.icons == None):
                            s += self.icons[self.board_list[y-1][x-1].state]
                        else:
                            s += str(self.board_list[y-1][x-1].state)
                    if(not x == self.width):
                        s += " "
            s += "\n"
        return s
    def __repr__(self):
        return str(self)
    def collapse(self):
        first = self.board_list[randint(0, self.height-1)][randint(0, self.width-1)].state
        self.board_list[randint(0, self.height-1)][randint(0, self.width-1)].state = first[randint(0, len(first)-1)]
        stop = False
        while True:
            self.updateBoard()
            best = [None, None]
            for y in range(self.height):
                for x in range(self.width):
                    if(type(self.board_list[y][x].state) is list):
                        if(best[0] == None):
                            best = [y, x]
                        if(len(self.board_list[y][x].state) < len(self.board_list[best[0]][best[1]].state)):
                            best = [y, x]
            if(best[0] == None):
                for y in range(self.height):
                    for x in range(self.width):
                        if(type(self.board_list[y][x].state) is list):
                            return False
                return True
            else:
                s = self.board_list[best[0]][best[1]].state
                self.board_list[best[0]][best[1]].state = s[randint(0, len(s)-1)]
                        
    def updateBoard(self):
        for y in range(self.height):
            for x in range(self.width):
                if(type(self.board_list[y][x].state) is list):
                    shouldChange = False
                    possible = rules.variants.copy()
                    for p in self.rules.positions:
                        if(x+p[0] < self.width and x+p[0] >= 0 and y+p[1] < self.height and y+p[1] >= 0):
                            for item1 in self.board_list[y][x].state:
                                item2 = self.board_list[y+p[1]][x+p[0]].state
                                if(type(item2) is int):
                                    r = Rule(p, item1, item2)
                                    if(not r in self.rules.rules and item1 in possible):
                                        possible.remove(item1)
                                        shouldChange = True
                    if(shouldChange):
                        self.board_list[y][x].state = possible

class Rule:
    def __init__(self, direction, item1, item2):
        self.direction = direction
        self.item1 = item1
        self.item2 = item2
    def __eq__(self, other):
        if(self.direction == other.direction):
            if(self.item1 == other.item1 and self.item2 == other.item2):
                return True
        return False
    def __str__(self):
        return f"({self.direction}, {self.item1}, {self.item2})"
    def __repr__(self):
        return f"({self.direction}, {self.item1}, {self.item2})"

class RuleSet:
    def __init__(self, example, n=1, isTile=False):
        self.variants = []
        self.rules = []
        self.isTile = isTile
        self.positions = []
        for x in range(-n, n+1):
            for y in range(-n, n+1):
                self.positions.append((x,y))
        for y in range(len(example)):
            for x in range(len(example[0])):
                if(not example[y][x] in self.variants):
                    self.variants.append(example[y][x])
                if(not isTile):
                    for p in self.positions:
                        if(x+p[0] <= len(example[0])-1 and x+p[0] >= 0 and y+p[1] <= len(example)-1 and y+p[1] >= 0):
                            rule = Rule(p, example[y][x], example[y+p[1]][x+p[0]])
                            if(not rule in self.rules):
                                self.rules.append(rule)

example_line =  [[0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0]]

example_dots =  [[0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0]]

example_blank = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

example_grid =  [[1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]]

example_hash =  [[1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1]]

example_three =[[1, 2, 0, 1, 2, 0],
                 [1, 2, 0, 1, 2, 0],
                 [1, 2, 0, 1, 2, 0],
                 [1, 2, 0, 1, 2, 0],
                 [1, 2, 0, 1, 2, 0],
                 [1, 2, 0, 1, 2, 0]]

example_diagonal =  [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0]]

while True:
    pattern = input("""
Which pattern would you like to see?
------------------------------------
1) Lines
2) Dots
3) Blank
4) Grid
5) Hash
6) Three lines
7) Diagonal

>>> """)

    if(pattern == "1"):
        rules = RuleSet(example_line, n=1)
    elif(pattern == "2"):
        rules = RuleSet(example_dots, n=1)
    elif(pattern == "3"):
        rules = RuleSet(example_blank, n=1)
    elif(pattern == "4"):
        rules = RuleSet(example_grid, n=2)
    elif(pattern == "5"):
        rules = RuleSet(example_hash, n=1)
    elif(pattern == "6"):
        rules = RuleSet(example_three, n=2)
    elif(pattern == "7"):
        rules = RuleSet(example_diagonal, n=1)

    board = Board(15, 15, rules)
    board.collapse()
    board.setIcons({0:"-", 1:"O", 2:"H"})
    print(board)
