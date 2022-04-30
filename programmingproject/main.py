import timeit
import numpy as np

#Brute Force
def findMajorityBF(arr):
    n = len(arr)
    maxCount = 0
    index = -1
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
        return -1

#Divide-and-Conquer
def FindMajorityDC(arr):
    n = len(arr)

    if(n == 2):
        #If the array has just two elements compare the two, if matched then return if not return -1
        if(arr[0] == arr[1]):
            return arr[0]
        else:
            return -1
    #If the array has one element then return that element
    elif(n == 1):
        return arr[0]

    #Splitting array in half and find majority in each half.
    leftMajority = FindMajorityDC(arr[:len(arr)//2]) #First half
    rightMajority = FindMajorityDC(arr[len(arr)//2:]) #Second half

    #If the left majority and the right majority are the same that means its the majority for the whole array
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
    m = {} #initialzing hashmap to store the element along with its key (an element's frequency)
    #Traversing array to insert elements to hashmap
    for i in range(n):
        #If an element appeared before increase key value by 1 else initalize key value to be 1
        if (arr[i] in m):
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    count = 0
    #Traversing hashmap to check if a key value for an element is greater then the frequency
    for key in m:
        if (m[key] > n / 2):
            count = 1
            return key
            break
    if(count == 0):
        return -1

#Generate random array with given size

# Driver code
arr = np.random.randint(100, size=1*(10**3))
print("If a function returns -1 then the array has no majority element")
# Function calling

#Brute Force
bf_start = timeit.default_timer()
print("Result of BF:", findMajorityBF(arr))
bf_end = timeit.default_timer()
print(bf_end-bf_start)

#Divide and Conquer
dc_start = timeit.default_timer()
print("Result of DC:", FindMajorityDC(arr))
dc_end = timeit.default_timer()
print(dc_end-dc_start)

#Hashmap
hm_start = timeit.default_timer()
print("Result of Hashmap:", findMajorityHash(arr))
hm_end = timeit.default_timer()
print(hm_end-hm_start)


