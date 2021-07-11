

#insertion sort
#assuming the first element is sorted and then comparing the other with the sorted and then placing in the sorted order 
#if you are confused then go and check playing cards and get back here


#card 1 | card2 | card3 | card4 -->>  card3 | card 4 | card2 | card1 
#   4       3       1       2           1       2       3       4

def insertion_sort(nums):
    for i in range(1, len(nums)): #1->5,2,3,4
        item_to_insert = nums[i]  #1,15,28,6
        j = i - 1       #0,1,2,3
        while j >= 0 and nums[j] > item_to_insert:  #0>=0 and 9>1,-1>=0,1>=0 & 9>15,2>=0,15>28,3>=0 and 28>6,2>=0 &15>6,1>=0&9>6
            nums[j + 1] = nums[j]       #9-><-1,28-><-6,15-><-6,9-><-6
            j -= 1   
        print(nums)                   #2[1,9,15,6,28],1[1,9,6,15,28],0[1,6,9,15,28]
        nums[j + 1] = item_to_insert 


random_list_of_nums = [9, 1, 15, 28, 6]# ->[1,9,15,28,6]->[1,6,15,28,9]->[1,6,9,28,15]->[1,6,9,15,28]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)




#n=[3,2,6,7,9,1,0]





"""for i in range(1,len(ar)): #2 #3 #4
        item=ar[i]          #1  #9 #2
        if ar[i]<ar[i-1]:   #1<7 #9<7  #9<2
                ar[i]=ar[i-1]   #0 7 1 9 2   #1=7  9=2
                ar[i-1]=item                       #7=1 sorted [0,1,7,9,2]    #2=9 sorted ->[0,1,7,2,9]
                
print(ar)"""



"""ar=[7,0,1,9,2]
for i in range(1,len(ar)):  #1
    item=ar[i]  #0
    j=i-1   #0
    minu=0
    while a[j]>item and : 
        minu=j-1     #0
        j=-1 
    ar[i]=ar[i-1] 
    ar[minu]=item         
    print(ar)"""
       
            

"""ar=[7,0,1,9,2]  #[0, 1, 7, 9, 2]
for i in range(1,len(ar)):  #4
    item=ar[i]  #2
    j=i  #4=4
    minu=0 #0
    while ar[i]<ar[j-1] and j>0: #2<9 and 4>0  2<7 
        minu=j-1     #2 #3
        j-=1       #2 #3
        ar[i]=ar[i-1]   #2=9
        ar[minu]=item   #9=2      
    print(ar)"""



"""a=[7,0,1,9,2] 
for i in range(1,len(a)):  #1 #2 #3 #4
    item=a[i]   #0 #1 #9  #2
    j=i-1  #0  #1 #2 #3
    
    while item<a[j] and j>=0: #0<7 0:  1<7 1: 9<7 2: 2<9  3: 2<7 2: 2<1 1:
        a[j+1]=a[j] #assigning index 1st to zeroth index 0=7 ,1=7 ,2=9 ,2=7
        j-=1 #outofbond ,0,2,1
    a[j+1]=item #0=item #1=item ,9=9 ,7=2
    print(a) """#[0, 7, 1, 9, 2], [0, 1, 7, 9, 2],[0, 1, 7, 9, 2],[0, 1, 2, 7, 9]
