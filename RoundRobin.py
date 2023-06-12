# Round Robin Scheduling Quantum = 3

class RoundRobin:
    def ProcessData(self,tp):
        process =[]
        while tp<3 or tp >10:
            print("Invalid range! Please enter a range of number between 3 to 10")
            print()
            tp = int(input("Enter total number of processes to be scheduled: "))
        for i in range(tp):
            temp = []
            procID = int(input("Enter process number: "))
            arrivalTime = int(input(f"Enter arrival time for Process {procID}: "))
            burstTime = int(input(f"Enter burst time for Process {procID}: "))
            complete = False #false means it is not executed yet, true means execution complete
            temp.extend([procID, arrivalTime, burstTime, complete, burstTime, ])
            process.append(temp)
        timeQuantum = int(input("Enter the time quantum: "))
        RoundRobin.RRProcess(self, process, timeQuantum)

            

    def RRProcess(self, process, timeQuantum): 
        process.sort(key=lambda x: (x[1], x[2])) #Sort first by arrival time, then by burst time
        starting = []
        start = 0
        timeExit = []
        timeExit.append(start)
        procEx = [] #Executed process
        readyQueue = [] #Stores processes which have arrived
        sTime = 0
        

        while 1:
            normalQueue = []
            temporary = []
            #for every process that has arrived
            for i in range (len(process)):
                    #If arrival time is before the current Time and the process has not finished execution
                if process[i][1] <= sTime and process[i][3] == False:
                    boolCondition = False
                    if len(readyQueue)!= 0: #If next process is found in the readyqueue
                        for k in range(len(readyQueue)):
                            if process[i][0] == readyQueue[k][0]: 
                                boolCondition = True

                    if boolCondition == False: # If not present in the readyqueue
                        temporary.extend([process[i][0], process[i][1], process[i][2],process[i][4]])
                        readyQueue.append(temporary)
                        temporary =[]

                    if len(readyQueue) != 0 and len(procEx)!= 0: 
                        for k in range(len(readyQueue)):
                            if readyQueue[k][0] == procEx[len(procEx)-1]:
                                readyQueue.insert((len(readyQueue)-1), readyQueue.pop(k))

                elif process[i][3] == False:
                    temporary.extend([process[i][0], process[i][1], process[i][2],process[i][4]])
                    normalQueue.append(temporary)
                    temporary =[]

            if len(readyQueue) == 0 and len(normalQueue) == 0:
                break
            
            if len(readyQueue) != 0:
                if readyQueue[0][2] <= timeQuantum: #if Process <= Q finish execution
                    starting.append(sTime)
                    sTime = sTime + readyQueue[0][2]
                    eTime = sTime
                    timeExit.append(eTime)
                    procEx.append(readyQueue[0][0])
                    for j in range (len(process)):
                        if process[j][0] == readyQueue[0][0]:
                            break
                    process[j][2] = 0
                    process[j][3] = True
                    process[j].append(eTime)
                    readyQueue.pop(0)

                elif readyQueue[0][2] > timeQuantum:
                    starting.append(sTime)
                    sTime = sTime + timeQuantum
                    eTime = sTime
                    timeExit.append(eTime)
                    procEx.append(readyQueue[0][0])
                    for j in range (len(process)):
                        if process[j][0] == readyQueue[0][0]:
                            break
                    process[j][2] = process[j][2] - timeQuantum
                    readyQueue.pop(0)

            elif len(readyQueue) == 0:
                if sTime < normalQueue[0][1]:
                    sTime = normalQueue[0][1]
                if normalQueue[0][2] > timeQuantum:
                    starting.append(sTime)
                    sTime += timeQuantum
                    eTime = sTime
                    timeExit.append(eTime)
                    procEx.append([normalQueue[0][0]])
                    for j in range(len(process)):
                        if process[j][0] == normalQueue[0][0]:
                            break
                    process[j][2] = process[j][2]-timeQuantum

                elif normalQueue[0][2] <= timeQuantum:
                    starting.append(sTime)
                    sTime += normalQueue[0][2]
                    eTime = sTime
                    timeExit.append(eTime)
                    procEx.append(normalQueue[0][0])
                    for j in range(len(process)):
                        if process[j][0] == normalQueue[0][0]:
                            break
                    process[j][2] = 0
                    process[j][3] = True
                    process[j].append(eTime)
        tTime = RoundRobin.TurnAroundTime(self, process)
        wTime = RoundRobin.WaitingTime(self, process)
        RoundRobin.Print(self,process,tTime, wTime, procEx,timeExit)

    def TurnAroundTime(self,process):
        totalTATime = 0
        for i in range(len(process)):
            TurnAroundTime = process[i][5] - process[i][1]
            totalTATime += TurnAroundTime
            process[i].append(TurnAroundTime)
        averageTATime = totalTATime/len(process)
        return averageTATime

    def WaitingTime(self,process):
        totalWTime = 0
        waiting =[]
        for i in range(len(process)):
            waiting = process[i][6] - process[i][4]
            totalWTime = totalWTime + waiting
            process[i].append(waiting)
        averageWaitingTime = totalWTime / len(process)
        return averageWaitingTime

          
    def Print(self,process,averageTATime,averageWaitingTime, procEx, timeExit):
        from tabulate import tabulate
        print("")
        print("Process Table")
        print("")
        printProc = [[p[0], p[1], p[4], p[5],p[6],p[7]] for p in process]
        print(tabulate(printProc, headers =[ "Process",  "Arrival Time",  "Burst Time", "Finish Time", "Turnaround Time",  "Waiting Time"]))
        print("")
        print("")
        print("Gantt Chart")
        for i in procEx:
            print("+------", end="")
        print("")
        for i in range(len(procEx)):
            print(f'| P{procEx[i]}', end = "   ")
        print("")

        for i in procEx:
            print("+------", end="")
        print("")

        for i in range(len(timeExit)):
            print("", timeExit[i], end ="    ")




        print("")
        print()
        print("Average Turn-Around Time: {:0.2f} ms".format(averageTATime))
        print("Average Waiting Time: {:0.2f} ms".format(averageWaitingTime))

       
       
if __name__ == "__main__":
    tp = int(input("Enter the total processes to be scheduled: "))
    rr = RoundRobin()
    rr.ProcessData(tp)










                

                
 
        



        



