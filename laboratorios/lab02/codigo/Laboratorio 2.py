import timeit
def insertion_sort (array):
    for i in range (1,len(array)):
        a = array [i]
        i = i-1
        while i>= 0:
            if a <array[i]:
                array [i+1] = array [i]
                array [i] = a
                i = i-1
            else: 
                break
n = 7000
array =[0]*n
for i in range (0,n):
    array [i] = n-i
    
start = timeit.default_timer()
insertion_sort (array)
stop = timeit.default_timer()
print('Time: ', stop - start)
#%%
# we used the code from https://dev.to/yogeswaran79/part-2-sorting-algorithm-17p5 for the merge sort algorithm
import timeit
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]  
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
       
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
     
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
 
n = 1221200


array =[0]*n
for i in range (0,n):
    array [i] = n-i

       
start = timeit.default_timer()
mergeSort(array)
stop = timeit.default_timer()
print('Time: ', stop - start)
