# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。

# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    result_str = ""

    word = ""
    for i in range(len(s)):
        if s[i] == " " and word != "":
            result_str = word + " " + result_str
            word = ""
        elif s[i] != " ":
            word += s[i]

        if i == len(s) - 1 and word != "":
            result_str = word + " " + result_str
        
    return result_str
        
        
            



if __name__ == "__main__":
    s = "a good   example"
    # "the sky is blue"  "  hello world  "
    result = reverseWords(s)
    print(result)