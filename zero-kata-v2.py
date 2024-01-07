from random import choice

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("I'm invincible you can't defeat me dummy don't even try\n(This is not arrogance this is a fact)\n")

def Checker(l1):
    # checking rows
    rowstrt = [0, 3, 6]
    for row in rowstrt:
        if l1[row] == l1[row + 1] == l1[row + 2]:
            winner = 'Computer' if l1[row]=='O' else 'You'
            print(f"{winner} won")
            return True

    # chekcing columns
    for i in range(3):
        if l1[rowstrt[0] + i] == l1[rowstrt[1] + i] == l1[rowstrt[2] + i]:
            winner = 'Computer' if l1[rowstrt[0]+i]=='O' else 'You'
            print(f"{winner} won")
            return True

    # checking diagonals
    if l1[0] == l1[4] == l1[8]:
        winner = 'Computer' if l1[row]=='O' else 'You'
        print(f"{winner} won")
        return True

    elif l1[2] == l1[4] == l1[6]:
        winner = 'Computer' if l1[row]=='O' else 'You'
        print(f"{winner} won")
        return True
    
    for i in l1:
        if type(i) == int: break
    else:
        print('This is a draw')
        return True

    return False


def printer(l1):
    for i in range(9):
        if i not in [1, 4, 7]:
            print("|", end="")
        print(f" {l1[i]}", end=" ")
        if i not in [1, 4, 7]:
            print("|", end="")
        if i in [2, 5, 8]:
            print()


def computerMove(l1,printyn=True):
    # horizontal
    attackOrDefense = {'O':'X', 'X':"O"}
    for katta in attackOrDefense: # now the computer can also win instead of playing defense only
    
        goldenPairs = {0: 3, 3: 6, 6: 9}

        for key in goldenPairs:
            if (
                l1[key : goldenPairs[key]].count(katta) == 2
                and attackOrDefense[katta] not in l1[key : goldenPairs[key]]
            ):
                for i in l1[key : goldenPairs[key]]:
                    if type(i) == int:
                        l1[l1.index(i)] = "O"
                        if printyn : printer(l1)
                        return
                break

        # vertical

        for strt in range(0, 3):
            verticalList = [l1[strt], l1[strt + 3], l1[strt + 6]] # Corrected incoreect logic 

            if verticalList.count(katta) == 2 and attackOrDefense[katta] not in verticalList:
                for i in verticalList:
                    if type(i) == int:
                        # l1[verticalList.index(i) * 3] = "O"
                        l1[i-1] = "O"
                        if printyn : printer(l1)
                        return
                break

        # diagonal

        diagonals = [[0, 4, 8], [2, 4, 6]]

        for diagonal in diagonals:
            items = [l1[diagonal[i]] for i in range(3)]
            if items.count(katta) == 2 and attackOrDefense[katta] not in items:
                for i in items:
                    if type(i) == int:
                        l1[l1.index(i)] = "O"
                        if printyn : printer(l1)
                        return
                break
            
        if katta == 'X':
            if l1.count('X') in [0,1]  and l1[4] not in ['X','O']:
                l1[4] = 'O'
                print('Iam here')
                
            else:
                options = [x for x in range(len(l1)) if type(l1[x]) != str]
                l1[choice(options)] = "O"

            if printyn : printer(l1)


wonORdraw = False
computerMove(l1,False)
printer(l1)
while not wonORdraw:

    inp = int(input("Choice: "))
    l1[l1.index(inp)] = "X"
    computerMove(l1,True)
    wonORdraw = Checker(l1)
