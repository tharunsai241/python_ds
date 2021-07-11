# python_ds

search alogrithms in python
linear search --> It sequentially checks each element of the list until a match is found or the whole list has been searched.best-case complexity is O(1) 
                  where the element is found at the first index. Worst-case complexity is O(n) where the element is found at the last index or element is not present in the array

binary search -->algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item,
                  until you've narrowed down the possible locations to just one.The time complexity of the binary search algorithm is O(log n). The best-case time complexity would be O(1) 
                  
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
_sorting algorithms_


**1.Bubble sort**:Sort by comparing each adjacent pair of items in a list in turn, swapping the items if necessary, and repeating the pass through the list until no swaps are   done. Also known as sinking sort, exchange sort time complexity is o(n^2).



 **2.Selection sort**: A sort algorithm that repeatedly searches remaining items to find the least one and moves it to its final location. The run time is Θ(n²), where n is the number of elements. The number of swaps is O(n).
 
 
 **3.Insertion sort**: Sort by repeatedly taking the next item and inserting it into the final data structure in its proper order with respect to items already inserted. Run time is O(n2) because of moves. Also known as linear insertion sort.
 
 
 **4.Quicksort**: Sort by repeatedly taking the next item and inserting it into the final data structure in its proper order with respect to items already inserted. Run time is O(n2) because of moves. Also known as linear insertion sort.
 
 
 **5.mergeSort**:Merge sort is a sorting technique based on divide and conquer technique. With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms. Merge sort first divides the array into equal halves and then combines them in a sorted manner.
