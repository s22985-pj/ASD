import time
import sys
import copy
import numpy as np

sys.setrecursionlimit(3000000)


def arrayRandom2000():
    arr = []
    for i in (np.array(range(0, 2000, 1))):
        arr.append(i)
    f = open('Sorted.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr

def arrayRandom4000():
    arr = []
    for i in (np.array(range(0, 4000, 1))):
        arr.append(i)
    f = open('Sorted.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr

def arrayRandom8000():
    arr = []
    for i in (np.array(range(0, 8000, 1))):
        arr.append(i)
    f = open('Sorted.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr

def arrayRandom16000():
    arr = []
    for i in (np.array(range(0, 16000, 1))):
        arr.append(i)
    f = open('Sorted.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr

def arrayRandom32000():
    arr = []
    for i in (np.array(range(0, 32000, 1))):
        arr.append(i)
    f = open('Sorted.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr


arr = arrayRandom2000()
arr1 = arrayRandom4000()
arr2 = arrayRandom8000()
arr3 = arrayRandom16000()
arr4 = arrayRandom32000()



def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above

    print("================Start==================\n")
    print("=======================================\n")


# Insertion sort
before_sort = arr

start_time_tree = time.time()

insertionSort(arr)
print(f"After sort with Insertion Sort: {arr} \n")
print(f"{time.time() - start_time_tree} seconds with sorted for n = 2000\n")
time1 = time.time() - start_time_tree

insertionSort(arr1)
print(f"After sort with Insertion Sort: {arr} \n")
print(f"{time.time() - start_time_tree} seconds with sorted for n = 4000\n")
time2 = time.time() - start_time_tree

insertionSort(arr2)
print(f"After sort with Insertion Sort: {arr} \n")
print(f"{time.time() - start_time_tree} seconds with sorted for n = 8000\n")
time3 = time.time() - start_time_tree

insertionSort(arr3)
print(f"After sort with Insertion Sort: {arr} \n")
print(f"{time.time() - start_time_tree} seconds with sorted for n = 16000\n")
time4 = time.time() - start_time_tree

insertionSort(arr4)
print(f"After sort with Insertion Sort: {arr} \n")
print(f"{time.time() - start_time_tree} seconds with sorted for n = 32000\n")
time5 = time.time() - start_time_tree

Fn1 = 2000/time1
Fn2 = 4000/time2
Fn3 = 8000/time3
Fn4 = 16000/time4
Fn5 = 32000/time5

print("================Best Case==================\n")
print(f"Fn/Tn dla n = 2000: {Fn1} \n")
print(f"Fn/Tn dla n = 4000: {Fn2} \n")
print(f"Fn/Tn dla n = 8000: {Fn3} \n")
print(f"Fn/Tn dla n = 16000: {Fn4} \n")
print(f"Fn/Tn dla n = 32000: {Fn5} \n")


print("=======================================\n")