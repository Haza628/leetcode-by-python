# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
# 并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。


def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """

    sorted_citations = sorted(citations, reverse=True)

    print(sorted_citations)
    for i in range(len(sorted_citations)):
        if sorted_citations[i] < i + 1:
            return i
        
    return len(sorted_citations)



if __name__ == "__main__":
    citations = [11, 15]
    # [3,0,6,1,5] [1,3,1] [1] [0] [11, 15]
    result = hIndex(citations)
    print(result)