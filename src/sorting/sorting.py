# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    x = 0 # pointer
    y = 0 # pointer

    for i in range(elements): # take a look through the merged elements
        print(merged_arr)

        if x < len(arrA) and y < len(arrB):
            # which is less?
            if arrA[x] <= arrB[y]: 
                merged_arr[i] = arrA[x] # set value in x and increment count
                x += 1
            else:
                merged_arr[i] = arrB[y] # otherwise, set value in y and increment count
                y += 1
        elif x < len(arrA) and y is len(arrB): # does the array have all the elements?
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1: # base case
        mid = len(arr) // 2 # set up the midpoint

        a = arr[:mid] #split the halves between the left and the right
        b = arr[mid:]

        a = merge_sort(a) # halve down to 1 item in both sublists
        b = merge_sort(b)

        return merge(a, b) # helper function merges the lists back together
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass

# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass