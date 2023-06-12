class Priority:

    def processData(self, tp):
        processData = []
        while tp<3 or tp >10:
            print("Invalid range! Please enter a range of number between 3 to 10")
            print()
            tp = int(input("Enter total number of processes to be scheduled: "))
        for i in range(tp):
            temporary = []
            procID = int(input("Enter Process ID: "))

            arrivalTime = int(input(f"Enter Arrival Time for Process {procID}: "))

            burstTime = int(input(f"Enter Burst Time for Process {procID}: "))

            priority = int(input(f"Enter Priority for Process {procID}: "))

            temporary.extend([procID, arrivalTime, burstTime, priority, 0])
            processData.append(temporary)
        Priority.PriorityScheduling(self, processData)


    def PriorityScheduling(self, processData):
        starting = []
        exitTime = []
        sTime = 0
        exitTime.append(sTime)
        executedProcess = []
        processData.sort(key=lambda x: x[1])
        for i in range(len(processData)):
            rQ = []
            temp = []
            nQ = []
            for j in range(len(processData)):
                if (processData[j][1] <= sTime) and (processData[j][4] == 0):
                    temp.extend([processData[j][0], processData[j][1], processData[j][2], processData[j][3]])
                    rQ.append(temp)
                    temp = []
                elif processData[j][4] == 0:
                    temp.extend([processData[j][0], processData[j][1], processData[j][2], processData[j][3]])
                    nQ.append(temp)
                    temp = []
            if len(rQ) != 0:
                rQ.sort(key=lambda x: x[3])
                starting.append(sTime)
                sTime = sTime + rQ[0][2]
                eTime = sTime
                exitTime.append(eTime)
                executedProcess.append(rQ[0][0])
                for k in range(len(processData)):
                    if processData[k][0] == rQ[0][0]:
                        break
                processData[k][4] = 1
                processData[k].append(eTime)
            elif len(rQ) == 0:
                if sTime < nQ[0][1]:
                    sTime = nQ[0][1]
                starting.append(sTime)
                sTime = sTime + nQ[0][2]
                eTime = sTime
                exitTime.append(eTime)
                executedProcess.append(nQ[0][0])
                for k in range(len(processData)):
                    if processData[k][0] == nQ[0][0]:
                        break
                processData[k][4] = 1
                processData[k].append(eTime)
        t_time = Priority.calculateTurnaroundTime(self, processData)
        w_time = Priority.calculateWaitingTime(self, processData)
        Priority.printData(self, processData, t_time, w_time,executedProcess,exitTime)


    def calculateTurnaroundTime(self, processData):
        ttlTA = 0
        for i in range(len(processData)):
            TA = processData[i][5] - processData[i][1]
            ttlTA = ttlTA + TA
            processData[i].append(TA)
        average_TA = ttlTA / len(processData)
        return average_TA


    def calculateWaitingTime(self, processData):
        ttlWT = 0
        for i in range(len(processData)):
            WT = processData[i][6] - processData[i][2]
            ttlWT = ttlWT + WT
            processData[i].append(WT)
        average_WT = ttlWT / len(processData)
        return average_WT

    def printData(self, processData, average_TA, average_WT,executedProcess,exitTime):
        processData.sort(key=lambda x: x[0])
        from tabulate import tabulate
        print("")
        print("Process Table")
        print("")
        printProc = [[p[0], p[1], p[2], p[3] ,p[5],p[6],p[7]] for p in processData]
        print(tabulate(printProc, headers =[ "Process",  "Arrival Time",  "Burst Time", "Priority", "Finish Time", "Turnaround Time",  "Waiting Time"]))
        print("")
        print("")
        print("Gantt Chart")
        for i in executedProcess:
            print("+------", end="")
        print("")
        for i in range(len(executedProcess)):
            print(f'| P{executedProcess[i]}', end = "   ")
        print("")

        for i in executedProcess:
            print("+------", end="")
        print("")

        for i in range(len(exitTime)):
            print("", exitTime[i], end ="    ")
        print("")
        print()
        print("Average Turn-Around Time: {:0.2f} ms".format(average_TA))
        print("Average Waiting Time: {:0.2f} ms".format(average_WT))


if __name__ == "__main__":
    tp = int(input("Enter number of processes: "))
    priority = Priority()
    priority.processData(tp)