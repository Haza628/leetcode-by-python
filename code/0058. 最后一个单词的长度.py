# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    last_word_length = 0
    flag = 0
    for i in range(len(s)):
        reverse_id = len(s) - 1 - i
        if s[reverse_id] != ' ' and flag == 0:
            flag = 1
        if s[reverse_id] != ' ' and flag == 1:
            last_word_length += 1
        elif s[reverse_id] == ' ' and flag == 1:
            return last_word_length



    return last_word_length



if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    # "Hello World" "   fly me   to   the moon  "
    result = lengthOfLastWord(s)
    print(result)

