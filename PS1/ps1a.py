###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    dictCow = {}
    fileCow = open(filename, 'r')
    
    for eachLine in fileCow:
        line = eachLine.split(',')
        cowName = line[0]
        cowWeight = int(line[1].split('\n')[0])
        dictCow[cowName]=cowWeight
    return dictCow
class Cow(object):
    def __init__(self, n, w):
        self.name = n
        self.weight = w
    
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.name + ',' + str(self.weight)
def BuildCowShed(names, weights):
    cowShed = []
    for i in range(len(names)):
        cowShed.append(Cow(names[i],weights[i]))
    return cowShed
        
        
        
# Problem 2
def greedy_cow_transport(cowShed,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # cowsCopy = cows
    # cowsCopySorted = sorted(cowsCopy, key = cowsCopy.get)
    # cowNames = list(cowsCopySorted.keys())
    # cowWeights = list(cowsCopySorted.values())
    # result = []
    # totalWeight = 0.0
    
    cowShedCopy = list(cowShed)
    cowShedSorted = sorted(cowShedCopy,key = Cow.getWeight, reverse = True)
    tripList, result = [], []
    def takeATrip(cowShedSorted, limit):
        """ takes input a set of cows , and the transport limit"""
        totalWeight, result = 0.0 , []
        cowShedSortedReturned = cowShedSorted
        for i in range(len(cowShedSorted)):
            if totalWeight+cowShedSorted[i].getWeight()<=limit:
                result.append(cowShedSorted[i].getName())
                totalWeight+=cowShedSorted[i].getWeight()
        return (result)
    
    def updateCowShed(names,cowShedSorted):
        updatedCowShed = cowShedSorted
        for i in names:
            for k in range(len(updatedCowShed)):
                if i == updatedCowShed[k].getName():
                    updatedCowShed.remove(updatedCowShed[k])
                    break
        return  updatedCowShed
    
    while len(cowShedSorted)!=0:
        result = takeATrip(cowShedSorted,limit)
        tripList.append(result)
        cowShedSorted = updateCowShed(result,cowShedSorted)
        
    return (tripList,len(tripList))
 
#running Problem  2
        


    
    
    
    
    
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowCopy = cows
    
    def takeATrip(cowSet):
        """ takes a set of partitions of cows and returns the trip, returns/
        total weight of the trip and cowset on the trip"""
        tripWeight = 0
        
            
    def tripGen(k, cowNames):
        "generates all possible combinations of 'k' trips of cowNames"
        from ps1_partition import partitions 
        from ps1_partition import get_partitions
        tripsList = get_partitions(cowNames)
        tripsToConsider = []
        for i in tripsList:
            if len(i)==k:
                tripsToConsider.append(i)
        return tripsToConsider
    
    def tripWeightCheck(cowCopy,trip):
        "Checks if the weight of the trip exceeds the limit of transport"
        weight = 0
        for i in trip:
              weight += cowCopy[i]
        return weight <= limit     
    
    def tripListWeightCheck(cowCopy,tripList):
        """Checks if each trip in the trip list satisfies the weight limit"""
        weightCheck = True
        for eachTrip in tripList:
            weightCheck = tripWeightCheck(cowCopy,eachTrip)
            if weightCheck == False:
                return weightCheck
        return weightCheck
    
    def bestTripList(cowCopy,tripLists):
        """this functions takes the set of triplists generated and returns the/
        best triplist the satisfies the weight criteria """
        for tripList in tripLists:
            if tripListWeightCheck(cowCopy,tripList):
                return tripList
        return None
    
    def minimumNumTrips(cowCopy):
        "this functions returns the minium set of triplists"
        cowNames = list(cowCopy.keys())
        numberOfCows = len(cowNames)
        for numOfTrips in range(1,numberOfCows):
            tripLists = tripGen(numOfTrips,cowNames)
            bestListofTrips = bestTripList(cowCopy,tripLists)
            if bestListofTrips != None:
                return (bestListofTrips,numOfTrips)
        return 'No Trips Found'
      
    return minimumNumTrips(cowCopy)
          
            
            
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    import ps1_partition
    import time
    
    cowsDict = load_cows('ps1_cow_data.txt')
    cowCopy = cowsDict
    Cow_names = list(cowsDict.keys())       
    Cow_weights= list(cowsDict.values())  
    Cow_shed = BuildCowShed(Cow_names, Cow_weights)
    tripLimit = 10
    
    #Greedy Algorithm Call
    startGreedy = time.time()
    tripsGreedy = greedy_cow_transport(Cow_shed,tripLimit)
    print('Min no of trips = '+str(tripsGreedy[1]))
    print(tripsGreedy[0])
    endGreedy = time.time()
    greedyTime = endGreedy-startGreedy
    print('\n Greedy Alg time taken:' + str(greedyTime))

    #Bruteforce Algorithm Call
    startBruteForce = time.time()
    minTrips = brute_force_cow_transport(cowCopy)
    print('Min no of trips = '+str(minTrips[1]))
    print(minTrips[0])
    endBruteForce = time.time()
    bruteForceTime = endBruteForce - startBruteForce
    print('\n Brute Force Alg time taken:' + str(bruteForceTime))
