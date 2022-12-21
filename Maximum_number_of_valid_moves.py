import heapq

def max_moves ( nums ):
    count = 0
    
    while len(nums) > 0:
        #looping over the heap
        heapq.heapify(nums)
        # finding the minimum element subtracting one from it and adding it abck to the heap
        min_heap_num = heapq.heappop(nums)

        if min_heap_num != 0:
            abc = ( min_heap_num - 1)
            heapq.heappush(nums,abc)
        else:
            continue
        #converting it to max heap and pooing the first element and subtracting one from it.
        heapq._heapify_max(nums)
        max_heap_num = heapq._heappop_max(nums)

        if max_heap_num != 0:
            abc = ( max_heap_num - 1) 
            heapq.heappush(nums,abc)
            
        #this completes one operation and so increaing the count
        count += 1 
        #handling edge conditions
        if len(nums) == 2 and (nums[0] == 0 or nums[1] == 0):
            break
        
    return count