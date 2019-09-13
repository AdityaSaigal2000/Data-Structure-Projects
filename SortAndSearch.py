# Includes code for Merge, Quick, Bubble and Selection Sort. Linear and Binary search are also included. More to be added!

def BubbleSort(arr):
    for i in range (0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if(arr[j]<arr[j+1]):
                [arr[j],arr[j+1]]=swap(arr[j],arr[j+1])
    return arr

def SelectionSort(arr):
    for j in range(0,len(arr)-1):
        largest=0
        for i in range(0,len(arr)-1-j):
            if(i==0 or (arr[largest])<arr[i]):
                largest=i
        [arr[len(arr)-1],arr[largest]]=swap(arr[len(arr)-1],arr[largest])
    return arr

def Merge(arr,l,r):
    i=0
    j=0
    k=0
    while(i<len(arr)):
        #print(arr)
        if(j<len(l) and k<len(r)):
            if(l[j]<r[k]):
                arr[i]=l[j]
                j=j+1
            else:
                arr[i]=r[k]
                k=k+1
        elif(j==len(l)):
            arr[i]=r[k]
            k=k+1
        elif(k==len(r)):
            arr[i]=l[j]
            j=j+1
        i=i+1

def MergeSort(arr):
    if(len(arr)!=1):
        if(len(arr)%2==0):
            l=MergeSort(arr[0:int(len(arr)/2)])
        else:
            l=MergeSort(arr[0:int((len(arr)/2)-0.5)])
        if(len(arr)%2==0):
            r=MergeSort(arr[int(len(arr)/2):len(arr)])
        else:
            r=MergeSort(arr[int(len(arr)/2-0.5):len(arr)])
    
    if(len(arr)==1):
        Merge(arr,arr,arr)
    else:
        Merge(arr,l,r)
    return arr
arr=[]
for i in range (0,30000):
    arr=arr+[i]

def BinarySearch(arr,val):
    if(len(arr)%2==0):
        middle=int(len(arr)/2)
    else:
        middle=int(len(arr)/2-0.5)
    if(len(arr)==1 and arr[middle]!=val):
        return False
    if(val>arr[middle]):
        return BinarySearch(arr[middle+1:len(arr)],val)
    elif(val<arr[middle]):
        return BinarySearch(arr[0:middle],val)
    if(val==arr[middle]):
        return True
def Partition(arr,start,end):
    part=start
    for i in range (start,end):
        if(arr[i]<arr[end]):
            temp=arr[part]
            arr[part]=arr[i]
            arr[i]=temp
            part=part+1
    temp=arr[part]
    arr[part]=arr[end]
    arr[end]=temp
    return part
def QuickSortHelp(arr,start,end):
    if(start<end):
        partition=Partition(arr,start,end)
        QuickSortHelp(arr,start,partition-1)
        QuickSortHelp(arr,partition+1,end)
def QuickSort(arr):
    QuickSortHelp(arr,0,len(arr)-1)

#Driver Code
arr=[7,2,1,6,8,5,3,4]
QuickSort(arr)
print(arr)
arr=[7,2,1,6,8,5,3,4]
MergeSort(arr)
arr=[7,2,1,6,8,5,3,4]
BubbleSort(arr)
arr=[7,2,1,6,8,5,3,4]
SelectionSort(arr)
