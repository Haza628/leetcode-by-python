# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

# 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k。
import numpy as np
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    num_list = []
    for n in nums:
        if n != val:
            num_list.append(n)
    nums[:len(num_list)] = num_list

    
    return len(num_list)


nums = [0,1,2,2,3,0,4,2]
val = 2

result = removeElement(nums, val)
print(nums)
print(result)