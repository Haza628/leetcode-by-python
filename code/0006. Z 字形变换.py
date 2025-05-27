
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s
    
    n = len(s)
    group_num = numRows + numRows - 2

    n_group = len(s) // group_num + 1

    new_result = ''

    for i in range(numRows):
        for j in range(i, n, group_num):
            new_result += s[j]
            if (i != 0 and i != numRows - 1) and j + 2 * (numRows - i - 1) < n:
                new_result += s[j + 2 * (numRows - i - 1)]
               

            
    return new_result
        


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    print(result)



#     0    1     1
#     1    1    1
#     2    1   1
#     3    1  1
#     4    1 1 
#     5    11
#     6    1

# numRows = 7


# 2 * (numRows - i - 1)