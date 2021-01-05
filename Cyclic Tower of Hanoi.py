import sys

#function to determine the first peg to move and in which direction
def tower(disk):
    #determine the second largest disk to be moved to the final peg containing the largest disk
    maxdisk, cw, maxpin = lastmove(disk)
    #if all the disks are already stacked on the final peg, no moves will be needed
    if maxdisk == -1:
        moves = 0
    #othewise, determine number of moves needed
    else:
        moves = totalmoves(disk, cw, maxdisk-1, maxdisk, 0)
        if moves >= 0:
            #As alternate disks move in the opposite direction, determine direction of the smallest disk based on the movement of the 2nd largest disk.
            if (maxdisk - 1) % 2 == 0:
                if cw == 1:
                    cw = 0
                else: 
                    cw = 1
    #To output direction of first disk to move       
    if cw == 1: 
        cw = "clockwise"
    else:
        cw = "counterclockwise"
    #To output final peg    
    if maxpin == 0:
        maxpin = "A"
    elif maxpin == 1:
        maxpin = "B"
    else: 
        maxpin = "C"
    #To output which is the first disk to move
    if moves % 2 == 0:
        startfirst = "even"
    else:
        startfirst = "odd"

    return maxpin, moves, startfirst, cw

#recursive function to determine total number of moves by accumulating the number of moves from the 2nd largest disk to the smallest disk
def totalmoves(disk, cw, currdisk, maxdisk, oldtotal):      
    steps = move(disk, currdisk, maxdisk, cw)
    if cw == 1:
        cw = 0
    else: 
        cw = 1
    #for the 3 largest disks to be moved
    if maxdisk - currdisk < 3:
        newtotal = steps + oldtotal
    else: 
        if (oldtotal - steps) % 3 == 2:
            newtotal = 2*oldtotal + 1
        elif (oldtotal - steps) % 3 == 1:
            return -1
        else: 
            newtotal = 2*oldtotal
    #not possible if the number of moves is less than the number of disks to be moved
    if newtotal < (maxdisk-currdisk):
        return -1
    #return number of moves if the current disk is the smallest
    elif currdisk == 1:
        return newtotal
    #recursion until the smallest disk 
    else: 
        return totalmoves(disk, cw, currdisk-1, maxdisk, newtotal)

def lastmove(disk):
    maxdisk = 0
    #find the final pin containing the largest disk
    for i in range(0, len(disk)):
        if len(disk[i]) > 0:
            if maxdisk < max(disk[i]):
                maxdisk = max(disk[i])
                maxpin = i
    penult = maxdisk - 1
    cw = 2
    while penult >= 1:
        #find the 2nd largest disk
        for i in range(0,len(disk)):
            if penult in disk[i]:
                penultpin = i
        #determine direction to move 2nd largest pin with minimal moves
        if abs(maxpin-penultpin) > 1:
            if penultpin < maxpin:
                cw = 0
            else:
                cw = 1
            break
        elif abs(maxpin-penultpin) == 1:
            if penultpin < maxpin:
                cw = 1
            else: 
                cw = 0
            break
        else:
            penult -= 1
    if cw == 2:
        return -1, cw, maxpin
    else:
        return penult+1, cw, maxpin

#function to compute the number of moves needed to move a given disk to the final peg in the given direction
def move(disk, currdisk, maxdisk, cw):
    for i in range(0,len(disk)):
        if maxdisk in disk[i]:
            maxpin = i
        if currdisk in disk[i]:
            currpin = i
    if currpin == maxpin:
        steps = 0
    elif cw == 1:
        if maxpin > currpin:
            steps = maxpin - currpin
        else: 
            steps = maxpin + 3 - currpin
    else:
        if maxpin < currpin:
            steps = currpin - maxpin
        else:
            steps = currpin + 3 - maxpin
    return steps

       
num_line = int(sys.stdin.readline())
for _ in range(num_line):
    disk = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    result = tower(disk)
    if result[1] == 0:
        print(result[0], result[1])
    elif result[1] == -1:
        print("impossible")
    else:
        print(result[0], result[1], result[2], result[3])
