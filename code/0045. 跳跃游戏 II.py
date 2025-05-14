# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    max_postion = 0
    end = 0
    jump_count = 0

    for i in range(n - 1):
        if i + nums[i] > max_postion:
            max_postion = i + nums[i]
        if i == end:
            end = max_postion
            jump_count += 1
    return jump_count



if __name__ == "__main__":
    nums = [4,0,0,3,1,4,0,1,4,1,0]
    # [2,3,0,1,4] [1] [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3] [2,3,1,1,4] [1, 0] [1,1,1,1]
    result = jump(nums)
    print(result)

