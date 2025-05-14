def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = {}

    for n in nums:
        if n not in count.keys():
            count[n] = 1
        else:
            count[n] += 1
            
        if count[n] > len(nums)/2:
            return n
        
        


    

nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(result)
