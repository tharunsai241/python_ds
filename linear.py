#linear search comparing the elements and returning the place or index

arr=list(map(int,input().split()))
n=len(arr)
data=int(input())
for i in range(n):
    if data==arr[i]:
        print("search element is at index is ",i)
        print("the element is",arr[i])
