print("selection sort")

ar=[176,-272,-272,-45,269,-327,-945,176] #->[0,1,6,64,12]->[0,1,6,12,64]
#swap 1st element ->last
#increment counter
#considering the first element itself min index as it is sorted

for i in range(len(ar)):
    min=i #we assumed the first element is in right place(sorted)
    #print(min)
    #this for is for traversing and then selecting the minimum element
    for j in range(i+1,len(ar)):
        if ar[min] > ar[j]:
            #we assigned the minimum index now if not this condition will not satisfy stays out itself
            min=j
        #swapping the elements as well as incrementing the counter
    ar[i],ar[min]=ar[min],ar[i]
    print(ar)
         



