# 给你两个字符串 haystack 和 needle ，
# 请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
        
            




if __name__ == "__main__":
    haystack = "sahfvuisap"       
    # "leetcode"  "sadbutsad" sahfvuisap
    needle = "fvu"
    # "leeto"  "sad"  fvujsacp
    result = strStr(haystack, needle)
    print(result)