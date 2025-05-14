def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    major = 0
    count = 0
    
    for n in nums:
        if count == 0:
            major = n
        if n == major:
            count = count + 1
        else:
            count = count - 1

    return major

nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(result)

# 这方法只有在众数过半的时候才能用，不然选不出最多的那个数 [2,2,1,1,3,3,4,4,5,4]
