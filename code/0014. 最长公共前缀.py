# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = strs[0]
    for str in strs:
        if str == "":
            return ""
        for i in range(min(len(prefix), len(str))):

            if prefix[i] != str[i]:
                prefix = prefix[:i]
                break
            if  i == min(len(prefix), len(str)) - 1:
                prefix = prefix[:i+1]
 
        if prefix == '':
            return prefix
    return prefix


    

if __name__ == "__main__":
    strs = ["abab","aba",""]
    # ["flower", "flow", "flight"] ["dog","racecar","car"] ["ab", "a"] ["abab","aba",""]
    result = longestCommonPrefix(strs)
    print(result)