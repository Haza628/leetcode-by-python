# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

# 你需要按照以下要求，给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    candy_list = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candy_list[i] = candy_list[i-1] + 1
    for i in range(1, len(ratings)):
        if ratings[len(ratings) - 1 - i] > ratings[len(ratings) - i]:
            candy_list[len(ratings) - 1 - i] = max(candy_list[len(ratings) - 1 - i], candy_list[len(ratings) - i] + 1)

    # print(candy_list)
    return sum(candy_list)


if __name__ == "__main__":
    ratings = [1,2,87,87,87,2,1]
    # [1,0,2] [1,2,2] [1,2,87,87,87,2,1]
    result = candy(ratings)
    print(result)