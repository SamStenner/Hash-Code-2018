time =  0
rowNumber = None
columnNumber = None
vehicleNumber = None
ridesNumber = None
bonusFactor = None
rideList = []
totalTime = None
carList = []

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = True
    for line in file:
        elements = line.split(' ')
        if firstLine:
            firstLine = False
            global rowNumber
            rowNumber = elements[0]
            global columnNumber
            columnNumber = elements[1]
            global vehicleNumber
            vehicleNumber = elements[2]
            global ridesNumber
            ridesNumber = elements[3]
            global bonusFactor
            bonusFactor = elements[4]
            global totalTime
            totalTime = elements[5]
        else:
            # calculate distance
            # store distance in ride info in array
            rideInfo = elements
            rideInfo.append(0)# distance
            rideList.append(rideInfo)
        global carList
        carList = [[0,0] for number in vehicleNumber]


def calcWeightForCar(carPos, journey):
    lateTime = journey[5]
    distJourney = journey[6]
    distToStart = calc_dist(carPos[0], carPos[1], journey[0], journey[1])
    return lateTime - time - distToStart - distJourney

def calc_dist(x1, y1, x2, y2):
    d_x = abs(int(x1) - int(x2))
    d_y = abs(int(y1) - int(y2))
    return d_x + d_y

if __name__ == "__main__":
    readFile("a_example.in")
    for i in range(len(rideList)):
        rideList[i][6] = calc_dist(rideList[i][0], rideList[i][1], rideList[i][2], rideList[i][3])
    for i in rideList:
        print(i)




