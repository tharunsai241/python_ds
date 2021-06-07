#binary search this can be implemented in recursive method and also in iterative method
#to perform this one prelimary condition is that the array should be in a sorted order

#iterative method

def binary_serach(arr,n,low,high):
    while low<=high:

        mid=(low+high)//2

        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            high=mid-1

        else:
            low=mid+1
    return -1

arr=list(map(int,input().split()))
n=int(input())
reu=binary_serach(arr,n,0,len(arr)-1)
if reu!=-1:
    print("element present at index"+str(reu))
else:
    print("not found")


#binary serach recursive method

"""def binary_serach(arr,n,low,high):
    if high>=low:
        mid=(high+low)//2

        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            return binary_serach(arr,n,low,mid-1)
        else:
            return binary_serach(arr,n,mid+1,high)
    else:
        return -1
arr=list(map(int,input().split()))
n=int(input())
reu=binary_serach(arr,n,0,len(arr)-1)
print("the index is",reu)"""




#     """0 1 2 3 4 5 6
# """arr=4 5 6 7 8 9 10   ->9 

#     left | right | mid
#     0        6      3 arr[i]<n:
#     0       2       1

    
# 0 1 2 3 4 5  6
# 5 6 7 8 9 10 11

    
#     0      6    3  arr[mid]>required_element:
#                     high=mid-1

#     0       2   1  arr[i]==n:
#                             return"""
    
