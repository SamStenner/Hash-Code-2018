time =  0
rowNumber = None
columnNumber = None
vehicleNumber = None
ridesNumber = None
bonusFactor = None
rideList = None
totalTime = None
map = None
carPositionList = None

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = True
    for line in file:
        elements = line.split(' ')
        if firstLine:
            firstLine = False
            rowNumber = elements[0]
            columnNumber = elements[1]
            vehicleNumber = elements[2]
            ridesNumber = elements[3]
            bonusFactor = elements[4]
            totalTime = elements[5]
        else:
            # calculate distance
            # store distance in ride info in array
            rideInfo = elements
            rideInfo.append(None)# distance
            rideList.append(rideInfo)

        carPositionList = [[0,0] for  number in vehicleNumber]




