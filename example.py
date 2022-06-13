#Given is a Dictionary with Values
#the values indicate the distances between two locations

locations = ["A", "B", "C", "D"]
distances = { "AB" : 10, "BC" : 20, "CD" : 30}

#Write a function that returns the distances between two locations.
#Example: 
# Input is "AC", the function returns 30
# Input is "AB", the function returns 10
# Input is "AA", the function returns 0
# Input is "BD", the function returns 50

# Make sure that the function can also handle inverted inputs, e.g. "CA" also returns 30

def calculateDistance(locationCombination : str) -> int :
    locationsSorted = sorted(locationCombination) #Sorts locations alphabetically, returns list of chars
    locationsCombi = "".join(locationsSorted)     #Combines the chars into a string



    wayToGo = pathFromPlac1ToPlace2(locationsCombi)
    distance = 0
    for i in range(0, len(wayToGo) - 1):
        for key in distances:
            if wayToGo[i] in key and wayToGo[i+1] in key:
                distance += distances[key]
    return distance


#test the implementation
print("AC", calculateDistance("AC"))
print("CA", calculateDistance("CA"))
print("AA", calculateDistance("AA"))
print("CD", calculateDistance("CD"))
print("AD", calculateDistance("AD"))
#etc.

def pathFromPlac1ToPlace2(locationCombination : str) -> list[str]: #NameError: is not defined yet
    l = []
    location1 = locationCombination[0]
    location2 = locationCombination[1]
    if(location1 == location2): return [location1]
    else:
        isOnWay = False
        for key in distances:
            if key[0] == location1: #We have a starting point
                l.append(location1)
                isOnWay=True
            if key[1] == location2: #We have an endpoint
                l.append(location2)
                return l
            elif isOnWay:
                l.append(key[1])

print("Path from A to B", pathFromPlac1ToPlace2("AB"))
print("Path from A to D", pathFromPlac1ToPlace2("AD"))
print("Path from B to D", pathFromPlac1ToPlace2("BD"))

#We imagine a circle.
#We want to determine the shortest distance beetween two Places.
#We can go either way.
#Tip1:Auxiliary functions that give all intermediate stations.
#Tipp2:Use the Modulo  Operator to prevent Overflow.
