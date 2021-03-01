# Ivan Stus CS560
# Assignment 1 Question 1


import array
import random
import timeit
import matplotlib.pyplot as plt     #imported matplotlib for plotting purposes


def insertionSort(arr, arr2):
    insert_total_time = 0   #total time counter
    for i in range(1, len(arr)): 
        insert_start_time = timeit.default_timer()  #start time counter
        key = arr[i]   
        j = i-1
        while j >= 0 and key < arr[j] :  
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
        insert_end_time = timeit.default_timer()    #end time counter
        insert_total_time = ((insert_end_time - insert_start_time) + insert_total_time)     
        arr2.append(insert_total_time)      #adds time to array for plotting
    

def mergeSort(arr, arr2, time): 
    merge_start_time = timeit.default_timer()   #start counter    
    if len(arr) > 1:         
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]   
        mergeSort(L, arr2, time) 
        mergeSort(R, arr2, time)   
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
        merge_end_time = timeit.default_timer() #end counter   
        time = ((merge_end_time - merge_start_time) + time) #adds on time from previous call         
        arr2.append(time)         



#DRIVER
n = input("Enter array length: ")   #prompts user input
n = int(n)  #sets user input to int
insert_array = []   #initialize arrays needed for sorting/timekeeping 
insert_time = []
merge_array = []
merge_time = []
x_axis = [] #x-axis is user inputted length counted from [0 - n-1]
merge_total_time = 0  
#FILL
for i in range(n):  
    x_axis.append(i)    
    insert_array.append(random.randint(0,10000))    #sets arrays to random numbers from 0 to 10000
    merge_array.append(insert_array[i])
#FUCTION CALLS
insertionSort(insert_array, insert_time)    
mergeSort(merge_array, merge_time, merge_total_time)
insert_time.append(0)   #append 0 to balance out arrays
merge_time.append(0)
#PLOTTING
x1 = x_axis
y1 = insert_time
plt.plot(x1, y1, label = 'Insertion')   #x1,y1 = insertion line 
x2 = x_axis
y2 = merge_time
plt.plot(x2, y2, label = 'Merge')       #x2,y2 = merge line
plt.xlabel('N') 
plt.ylabel('T') 
plt.title('Insertion vs Merge Sort (n vs T)')  
plt.legend()  
plt.show() 