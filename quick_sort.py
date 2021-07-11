#quick sort

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            #element smaller than the pivot element
            #swapping it with the greater element
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1] 
    return i+1  


def quicksort(arr,low,high):
    if low<high: #pivot element finding
        p=partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

data = list(map(int,input().split()))
print("Unsorted Array")
print(data)

size = len(data)

quicksort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(*data)