# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result_left = [1] * len(nums)
    result_right = [1] * len(nums)
    result = [1] * len(nums)
    
    for i in range(1, len(nums)):
        result_left[i] = result_left[i - 1] * nums[i - 1]

    for i in range(1, len(nums)):
        i = len(nums) - i - 1
        result_right[i] = result_right[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        result[i] = result_left[i] * result_right[i]

    return result
        

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    # [1,2,3,4] [-1,1,0,-3,3]
    result = productExceptSelf(nums)
    print(result)

    