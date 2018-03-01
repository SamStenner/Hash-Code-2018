time =  0
rowNumber = None
columnNumber = None
vehicleNumber = None
ridesNumber = None
bonusFactor = None
rideList = []
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


readFile("a_example.in")
for i in carPositionList:
    print(i)



def calc_dist(ride_index):
    ride = rideList[ride_index]
    d_x = abs(ride[0] - ride[2])
    d_y = abs(ride[1] - ride[3])
    d_xy = d_x + d_y
    print(d_xy)

