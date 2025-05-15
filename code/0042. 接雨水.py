# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    p = 0
    q = len(height) - 1
    left = 0
    right = 0
    result = 0
    while p < q:
        if height[p] < height[q]:
            if height[p] > left:
                left = height[p]
            else:
                result += left - height[p]
            p += 1
        else:
            if height[q] > right:
                right = height[q]
            else:
                result += right - height[q]
            q -= 1
    return result
       
if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # [0,1,0,2,1,0,1,3,2,1,2,1] [4,2,0,3,2,5]
    result = trap(height)
    print(result)