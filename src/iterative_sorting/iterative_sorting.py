# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i #0
        smallest_index = cur_index #0
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
            # arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
            #just need to put smallest index where current index is
        current_current = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = current_current
            

    return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap is True:
        swap = False
        for i in range(0, len(arr) - 1):
            
            current_index = i 

            #if current value is greater than next swap
            if arr[current_index] > arr[current_index + 1]:
                current_val = arr[current_index]
                compare_val = arr[current_index + 1]

                arr[current_index] = compare_val
                arr[current_index + 1] = current_val

                swap = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
