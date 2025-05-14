def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """


    k = k % len(nums)
    for i in range(len(nums)-k):
        nums.append(nums.pop(0))







nums = [1, 2]
k = 3
rotate(nums, k)
print(nums)

    
        