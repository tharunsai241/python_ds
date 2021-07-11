#bubble sort u
#no of test cases
tc=int(input())
#taking the input
n=list(map(int,input().split()))
c=0
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            c+=1 #no of swaps by incrementing c
            n[j],n[j+1]=n[j+1],n[j]
print(n)
print(c)