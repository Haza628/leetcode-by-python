
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p = 1
    flag = 0
    for i in nums[1:]:
        if i != nums[p-1]:
            nums[p] = i
            p = p + 1
            flag = 0
        
        elif i == nums[p-1] and flag == 0:
            nums[p] = i
            p = p + 1
            flag = 1
    return p
    