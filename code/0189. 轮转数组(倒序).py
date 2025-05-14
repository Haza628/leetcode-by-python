def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """


    k = k % len(nums)
    nums[:len(nums) - k] = nums[:len(nums) - k][::-1]
    nums[len(nums) - k:] = nums[len(nums) - k:][::-1]
    nums[:] = nums[::-1]

    






nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
rotate(nums, k)
print(nums)

    
        