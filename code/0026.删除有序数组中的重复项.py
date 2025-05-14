
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p = 1
    for i in nums:
        if i != nums[p - 1]:
            nums[p] = i
            p += 1
    return p

if __name__ == "__main__":
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    n = removeDuplicates(nums)
    print(n, nums)
