
def bubble_sort(arr):
    swap_happed = True
    while swap_happed:
        print('bubble sort:   '+str(arr))
        swap_happed = False
        for num in range(len(arr)-1) :
            if arr[num]>arr[num+1]:
                swap_happed= True
                arr[num],arr[num+1]=arr[num+1],arr[num]
          



l=[6,8,1,4,10,7,8,9,3,2,5]
bubble_sort(l)