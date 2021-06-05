#merge sort
#has divide and conquer and recursion strategy

def merge(arr):
    if len(arr)>1:
        r=len(arr)//2
        l=arr[:r]
        #print(l)
        t=arr[r:]
        #print(t)
        merge(l)
        merge(t)
        i=k=j=0
        while i<len(l) and j<len(t):
            if l[i]<t[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=t[j]
                j+=1
            k+=1 #increments the index position in the actual solution
    
    #if some of the elements are run out in l or m then put the elements in the arr
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        
        while j<len(t):
            arr[k]=t[j]
            j+=1
            k+=1


arr = list(map(int,input().split()))
print(arr)

th = len(arr)
merge(arr)
print('Sorted Array in Ascending Order:')
print(*arr)
