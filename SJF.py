class SJF:

    def processData(self, tp):
        dataProc = []
        while tp<3 or tp >10:
            print("Invalid range! Please enter a range of number between 3 to 10")
            print()
            tp = int(input("Enter total number of processes to be scheduled: "))
        for i in range(tp):
            temporary = []
            procID = int(input("Enter Process Number: "))

            arrivalTime = int(input(f"Enter Arrival Time for Process {procID}: "))

            burstTime = int(input(f"Enter Burst Time for Process {procID}: "))
            temporary.extend([procID, arrivalTime, burstTime, 0])
            dataProc.append(temporary)
        SJF.schedulingProcess(self, dataProc)


    def schedulingProcess(self, dataProc):
        startTime = []
        exitTime = []
        s_time = 0
        exitTime.append(s_time)
        executedProcess = []
        dataProc.sort(key=lambda x: x[1])
        for i in range(len(dataProc)):
            rQ = []
            temp = []
            nQ = []

            for j in range(len(dataProc)):
                if (dataProc[j][1] <= s_time) and (dataProc[j][3] == 0):
                    temp.extend([dataProc[j][0], dataProc[j][1], dataProc[j][2]])
                    rQ.append(temp)
                    temp = []
                elif dataProc[j][3] == 0:
                    temp.extend([dataProc[j][0], dataProc[j][1], dataProc[j][2]])
                    nQ.append(temp)
                    temp = []

            if len(rQ) != 0:
                rQ.sort(key=lambda x: x[2])
                startTime.append(s_time)
                s_time = s_time + rQ[0][2]
                e_time = s_time
                exitTime.append(e_time)
                executedProcess.append(rQ[0][0])
                for k in range(len(dataProc)):
                    if dataProc[k][0] == rQ[0][0]:
                        break
                dataProc[k][3] = 1
                dataProc[k].append(e_time)

            elif len(rQ) == 0:
                if s_time < nQ[0][1]:
                    s_time = nQ[0][1]
                startTime.append(s_time)
                s_time = s_time + nQ[0][2]
                e_time = s_time
                exitTime.append(e_time)
                executedProcess.append(nQ[0][0])
                for k in range(len(dataProc)):
                    if dataProc[k][0] == nQ[0][0]:
                        break
                dataProc[k][3] = 1
                dataProc[k].append(e_time)

        t_time = SJF.calculateTurnaroundTime(self, dataProc)
        w_time = SJF.calculateWaitingTime(self, dataProc)
        SJF.printData(self, dataProc, t_time, w_time,executedProcess, exitTime)


    def calculateTurnaroundTime(self, dataProc):
        TotalTA = 0
        for i in range(len(dataProc)):
            TA = dataProc[i][4] - dataProc[i][1]
            TotalTA = TotalTA + TA
            dataProc[i].append(TA)
        average_TA = TotalTA / len(dataProc)
        return average_TA


    def calculateWaitingTime(self, dataProc):
        TotalWT = 0
        for i in range(len(dataProc)):
            WT = dataProc[i][5] - dataProc[i][2]
            TotalWT = TotalWT + WT
            dataProc[i].append(WT)
        average_WT = TotalWT / len(dataProc)
        return average_WT


    def printData(self, dataProc, average_TA, average_WT,executedProcess, exitTime):
        dataProc.sort(key=lambda x: x[0])
        from tabulate import tabulate
        print("")
        print("Process Table")
        print("")
        printProc = [[p[0], p[1], p[2], p[4],p[5],p[6]] for p in dataProc]
        print(tabulate(printProc, headers =[ "Process",  "Arrival Time",  "Burst Time", "Finish Time", "Turnaround Time",  "Waiting Time"]))
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
    sjf = SJF()
    sjf.processData(tp)
