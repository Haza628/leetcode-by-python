# 给你两个字符串 haystack 和 needle ，
# 请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    start_p = -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and start_p == -1 and i + len(needle) <= len(haystack):
            start_p = i
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    start_p = -1
                    break
    return start_p
            




if __name__ == "__main__":
    haystack = "sahfvuisap"       
    # "leetcode"  "sadbutsad" sahfvuisap
    needle = "fvu"
    # "leeto"  "sad"  fvujsacp
    result = strStr(haystack, needle)
    print(result)