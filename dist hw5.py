
import random

K = [5,20,100] # Number of processors.
finalans = [] # Array of total number of cycles each k value takes to reach a steady state.
loadsList = [] # Array containing the loads distributed among processors, when it converges.

# Determines whether the processors have reached a steady state.
# Input: Array of intergers, which represent the load on each processor
# Output: True or False (Load is balanced or not)
def isBalanced(array):
    highest = max(array)
    lowest = min(array)
    if(highest - lowest > 2):
        return False
    return True

for k in K:

    LBCycle = [] # The number of cycles after which each processor gets a load.
    loadUnits = [] # The amount of load each processor gets.
    
    for i in range(k):
        # Load on each processor: Random number generated with Uniform distribution from 10 to 1000.
        load_Pi = int(random.uniform(10,1000))
        loadUnits.append(load_Pi)
    for i in range(k):
        # Time cycle at which the processor much balance its load: Random number generated with Uniform distribution from 100 to 1000.
        LB_i = int(random.uniform(100,1000))
        LBCycle.append(LB_i)

    print ("Load Units on processors at the begining: ",loadUnits)
    print ("LB Cycle array: ",LBCycle)
    # print ("****************************************************************")    

    executedCycles = 0
    totalExecutedCycles = 0 # Total number of executed cycles. This is our answer. 

    # Upper limit: 5,000,000 cycles.
    # Will run until the number of cycles reaches 5 Million, OR the loads get balanced.
    while(totalExecutedCycles < 5000000 and (not isBalanced(loadUnits))): # isBalanced() method implemented above

        # Loops over to zero (if loads are not balanced), and runs until the loads are balanced
        if(executedCycles > 1000):
            executedCycles = 0

        # Check which decides whether the current processor must load balance or not
        if(executedCycles in LBCycle):
            # Get the index in LBCycle array, which corresponds to the respective processor.
            p = LBCycle.index(executedCycles)

            # Perform load balancing for Processor p.
            if(p < k-1):
                # To ensure that each processor only 'gives' load, and doesn't 'take' load from neighbors.
                if(loadUnits[p] < loadUnits[((p-1) % k)] and loadUnits[p] < loadUnits[(p+1) % k]): 
                    z=1 # Do nothing if load on Processor p in lesser than its neighbors. 
                else:    
                    curSum = loadUnits[p] + loadUnits[p-1] + loadUnits[p+1]
                    curAvg = int(round(curSum/3))
                    loadUnits[p] = curAvg
                    loadUnits[p-1] = curAvg
                    loadUnits[p+1] = curSum - (loadUnits[p] + loadUnits[p-1]) # To ensure the sum of the triplets is never changed after load balancing
            
            else: # If p = k-1 --> it means if p is pointing to the last element in loadUnits, then we must loop around

                # To ensure that each processor only 'gives' load, and doesn't 'take' load from neighbors
                if(loadUnits[p] < loadUnits[(p-1)%k] and loadUnits[p] < loadUnits[0]):
                    z=1 # Do nothing if load on Processor p in lesser than its neighbors. 
                else:
                    curSum = loadUnits[p] + loadUnits[p-1] + loadUnits[0]
                    curAvg = int(round(curSum/3))
                    loadUnits[p] = curAvg
                    loadUnits[p-1] = curAvg
                    loadUnits[0] = curSum - (loadUnits[p] + loadUnits[p-1])

            # Setting a new random time cycle for load balancing of processor p
            LBCycle[p] = int(random.uniform(0,1000))
            # print ("\n*******************************")
            # print ("New LB Cycle: ", LBCycle)
            # print ("*******************************\n")

        executedCycles += 1
        totalExecutedCycles += 1

    # If loadUnits is balanced, then return the value of totalExecutedCycles
    finalans.append((k,totalExecutedCycles))
    loadsList.append(loadUnits)

# Array of tuples --> (k,totalExecutedCycles)
print ("*****************************************************")
print ("\nFor each case of no. of processors, the no. of cycles it takes to converge is as follows: {} \n".format(finalans))      
print ("\nThe distributed loads look like this, after converging: ")
for l in loadsList:
    print (l)
    print ('\n')
