
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
    if numRows == 1:
        return s
    
    

    group_num = numRows + numRows - 2

    n_group = len(s) // group_num + 1

    result = [[" "] * (numRows * (n_group + 1)) for _ in range(numRows) ]

   

    for i in range(len(s)):
        
        group_index = i // group_num
        in_group_index = i % group_num
        
        if in_group_index == 0:
            result_index_row = 0
            result_index_col = group_index * (numRows-1)
            

        elif in_group_index == numRows - 1:
            result_index_row = numRows - 1
            result_index_col = group_index * (numRows-1)
            

        elif in_group_index < numRows:
            result_index_row = in_group_index
            result_index_col = group_index * (numRows-1)
           

        else:
            result_index_row = group_num - in_group_index
            result_index_col = group_index * (numRows-1) + in_group_index - numRows + 1
            

        result[result_index_row][result_index_col] = s[i]

        new_result = ""
        for r in result:
            for str in r:
                if str != " ":
                    new_result += str


            
    return new_result
        

        


        





if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    print(result)
