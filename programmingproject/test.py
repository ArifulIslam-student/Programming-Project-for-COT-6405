import numpy as np
import timeit

#Brute Force
def findMajorityBF(arr):
    n = len(arr)
    maxCount = 0
    index = -1 # sentinels
    for i in range(n):

        count = 0
        for j in range(n):

            if(arr[i] == arr[j]):
                count += 1

        # update maxCount if count of
        # current element is greater
        if(count > maxCount):

            maxCount = count
            index = i

    # if maxCount is greater than n/2
    # return the corresponding element
    if (maxCount > n/2):
        return arr[index]

    else:
        return -1;

#Divide-and-Conquer
def FindMajorityDC(arr):
    n = len(arr);

    if(n == 2):
        #If a has just two elements, we just need to compare the two.
        if(arr[0] == arr[1]):
            #They are the same, so they are the majority element of a.
            #That is because they appear more than l/2 times.
            #Return them.
            return arr[0];
        else:
            #They aren't the same, so a doesn't have a majority element
            #Return -1. We treat -1 as a non-element.
            return -1;
    elif(n == 1):
        return arr[0]

    #Find the majority elements (if they exist) of the two halves.
    leftMajority = FindMajorityDC(arr[:len(arr)//2]); #First half
    rightMajority = FindMajorityDC(arr[len(arr)//2:]); #Second half

    #if the left majority and the right majority are the same that means its the majority for the whole array
    if (leftMajority == rightMajority):
        return leftMajority

    #If not the array needs to be counted to see how many times the left majority and right majority occurs
    leftCount = 0
    rightCount = 0
    for i in range(n):
        if (arr[i] == leftMajority):
            leftCount = leftCount + 1
        if (arr[i] == rightMajority):
            rightCount = rightCount + 1

    #Checking if either the left count or right count are greater than to the frequency
    if (leftCount > n / 2):
        return leftMajority
    elif (rightCount > n / 2):
        return rightMajority
    else:
        return -1

#Hashmap
def findMajorityHash(arr):
    n = len(arr)
    m = {}
    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    count = 0
    for key in m:
        if (m[key] > n / 2):
            count = 1
            return key
            break
    if(count == 0):
        return -1;
#Driver
# 1 is the majority element
arr = [1, 1, 2, 1, 3, 5, 1]

print("Result of BF:", findMajorityBF(arr))
print("Result of DC:", FindMajorityDC(arr))
print("Result of Hashmap:", findMajorityHash(arr))

print(" ")
# There is no majority element so -1 should be returned
arr2 = [3, 3, 1, 1, 2, 2, 2, 1]
print("Result of BF:", findMajorityBF(arr2))
print("Result of DC:", FindMajorityDC(arr2))
print("Result of Hashmap:", findMajorityHash(arr2))
