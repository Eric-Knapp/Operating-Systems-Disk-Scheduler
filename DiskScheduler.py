'''
These are implementations of different disk scheduling algorithms
in python. They were written using a more algorithmic approach
rather than using the various list functions that are available
in python. 

Usage: python DiskScheduler.py <initial cylinder position>

i.e.
python DiskScheduler.py 2150
'''
import sys

import pdb

LEFT = "LEFT"
RIGHT = "RIGHT"

LOWER_CYLINDER = 0
UPPER_CYLINDER = 4999

'''
SSTF algorithm
'''
def SSTF(requests, initialPosition):
    localRequests = list(requests)
    
    position = initialPosition
    movement = 0
    
    while localRequests:
        #find the closest request to the current cylinder
        closest = abs(position - localRequests[0])
        closestIndex = 0
        for x in range(1, len(localRequests)):
            if abs(position - localRequests[x]) < closest:
                closest = abs(position - localRequests[x])
                closestIndex = x
                
        movement += abs(position - localRequests[closestIndex]) 
        position = localRequests[closestIndex]
        print("Servicing " + str(position))
        localRequests.remove(position)      
        
    return movement

'''        
FCFS algorithm
'''
def FCFS(requests, initialPosition):
    position = initialPosition
    movement = 0
   
    for x in range(len(requests)):
        movement += abs(position - requests[x])
        position = requests[x]
        print("Servicing " + str(position))
        
    return movement

''' 
SCAN algorithm
'''
def SCAN(requests, initialPosition):
    direction = RIGHT
    localRequests = list(requests)
    position = initialPosition
    movement = 0

    while localRequests:
        #pdb.set_trace() 
        if position in localRequests:
            print("Servicing " + str(position))
            localRequests.remove(position)

            if not localRequests:
                break

        if direction == LEFT and position > LOWER_CYLINDER:
            position -= 1
        if direction == RIGHT and position < UPPER_CYLINDER:
            position += 1

        movement += 1

        if position == 0:
            direction = RIGHT
        if position == UPPER_CYLINDER:
            direction = LEFT

    return movement


'''
C-SCAN algorithm
'''
def C_SCAN(requests, initialPosition):
    localRequests = list(requests)
    position = initialPosition
    movement = 0

    while localRequests:
        if position in localRequests:
            print("Servicing " + str(position))
            localRequests.remove(position)

            if not localRequests:
                break
    
        movement += 1
        position += 1
        if position == UPPER_CYLINDER:
            position = 0
            movement += UPPER_CYLINDER

    return movement

'''
LOOK algorithm
'''
def LOOK(requests, initialPosition):
    direction = RIGHT
    localRequests = list(requests)
    localRequests.sort()
    position = initialPosition
    movement = 0

    while localRequests:
        if position <= localRequests[0]:
            direction = RIGHT
        if position >= localRequests[-1]:
            direction = LEFT

        if position in localRequests:
            print("Servicing " + str(position))
            localRequests.remove(position)

            if not localRequests:
                break

        if direction == LEFT and position > LOWER_CYLINDER:
            position -= 1
        if direction == RIGHT and position < UPPER_CYLINDER:
            position += 1
    
        movement += 1

    return movement

'''
C-LOOK algorithm
'''
def C_LOOK(requests, initialPosition):
    localRequests = list(requests)
    localRequests.sort()
    position = initialPosition
    movement = 0

    while localRequests:
        if position in localRequests:
            print("Servicing " + str(position))
            localRequests.remove(position)
            
            if not localRequests:
                break
        
        if position > localRequests[-1]:
            movement += abs(position - localRequests[0])
            position = localRequests[0]
        else:
            movement += 1
            position += 1
           

    return movement


#main function
if __name__ == '__main__':
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    #requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
    #requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
	
    initialPosition = int(sys.argv[1])
#    initialPosition = 2150
    
    print("\tFCFS = " + str(FCFS(requests, initialPosition)))
    
    print("\tSSTF = " + str(SSTF(requests, initialPosition)))
    
    print("\tSCAN = " + str(SCAN(requests, initialPosition)))
    
    print("\tC-SCAN = " + str(C_SCAN(requests, initialPosition)))
    
    print("\tLOOK = " + str(LOOK(requests, initialPosition)))
    
    print("\tC-LOOK = " + str(C_LOOK(requests, initialPosition)))

    x = input("Pausing program, press Enter to quit")
