time = 0
rowNumber = None
columnNumber = None
vehicleNumber = None
ridesNumber = None
bonusFactor = None
rideList = []
totalTime = None
carList = []
takenRideList = []

def readFile(fileName):
    file = open(fileName, 'r')
    firstLine = True
    for line in file:
        elements = line.split(' ')
        if firstLine:
            firstLine = False
            global rowNumber
            rowNumber = int(elements[0])
            global columnNumber
            columnNumber = int(elements[1])
            global vehicleNumber
            vehicleNumber = int(elements[2])
            global ridesNumber
            ridesNumber = int(elements[3])
            global bonusFactor
            bonusFactor = int(elements[4])
            global totalTime
            totalTime = int(elements[5])
        else:
            elements[5] = elements[5].strip('\n')
            for i in range(0, len(elements)):
                elements[i] = int(elements[i])
            elements.append(False)
            elements.append(calc_dist(elements[0], elements[1], elements[2], elements[3]))
            rideInfo = elements
            rideList.append(rideInfo)
        global carList
        carList = [[0, 0, False, None] for number in range(0, vehicleNumber)]
    file.close()


def calc_car_weight(carX, carY, ride):
    lateTime = int(ride[5])
    distJourney = int(ride[6])
    distToStart = calc_dist(carX, carY, ride[0], ride[1])
    return lateTime - time - distToStart - distJourney


def calc_dist(x1, y1, x2, y2):
    d_x = abs(int(x1) - int(x2))
    d_y = abs(int(y1) - int(y2))
    return d_x + d_y


def simulate():
    global time
    global totalTime
    time = 0
    finished = False
    for car in carList:
        car[3] = select_journey(car)
    while not finished:
        for carIndex, car in enumerate(carList, 0):
            if car is None:
                continue
           # print("")
           # print("Car " + str(carIndex) + ": ")
           # print(car[0], car[1], car[2])
           # print(car[3])
            if car[2] == False:
                ride = rideList[car[3]]
                if car[0] == ride[0] and car[1] == ride[1] and time >= ride[4]:
                    car[2] = True
                else:
                    x, y = update_car_coords(car[0], car[1], ride[0], ride[1])
                    car[0] = x
                    car[1] = y
            if car[2] == True:
                current_ride = rideList[car[3]]
                if car[0] == current_ride[2] and car[1] == current_ride[3]:
                    journey = select_journey(car)
                    if journey != -1:
                        car[3] = journey
                    else:
                        carList[carIndex] = None
                        assignRideOutput(carIndex, car[3])
                else:
                    car[0], car[1] = update_car_coords(car[0], car[1], current_ride[2], current_ride[3])
        if time < totalTime:
            time += 1
        else:
            finished = True
    for lineInfo in takenRideList:
        print(lineInfo)
    print("Simulation finished")


def select_journey(car):
    car[2] = False
    best_score = 99999999999999
    best_ride_index = -1
    for i in range(0, len(rideList)):
        if rideList[i][6] == False:
            score = calc_car_weight(car[0], car[1], rideList[i])
            if score < best_score:
                best_ride_index = i
                best_score = score
    rideList[best_ride_index][6] = True
    return best_ride_index


def update_car_coords(x1, y1, x2, y2):
    if x1 != x2:
        if x1 > x2:
            x1 = x1 - 1
        else:
            x1 = x1 + 1
    else:
        if y1 > y2:
            y1 = y1 - 1
        else:
            y1 = y1 + 1
    return x1, y1

def assignRideOutput(carNum, rideNum):
    global takenRideList
    takenRideList[carNum][0] = takenRideList[carNum][0]+1
    takenRideList[carNum][1].append(int(rideNum))

def writeOutputFile(name):
    file = open(name+".txt", "w")
    for lineInfo in takenRideList:
        rideList = ""
        for ride in lineInfo[1]:
            rideList = rideList + format("%d " % ride)
        file.write(format("%d %s\n" % (int(lineInfo[0]), rideList)))
    file.close()

if __name__ == "__main__":
    readFile("c_no_hurry.in")
    takenRideList = [[0, []] for int in range(vehicleNumber)]
    simulate()
    writeOutputFile("test2.in")




