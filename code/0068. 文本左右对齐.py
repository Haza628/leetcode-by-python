# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。

# 注意:

# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    # 处理特殊情况
    if len(words) == 1:
        return [words[0] + ' ' * (maxWidth - len(words[0]))]

    # 构造输出行结构
    words_row = words[0]
    word_row_list = [words[0]]
    result = []
    all_word_list = []
    for i in range(1, len(words)):
        if len(words_row + ' ' + words[i]) > maxWidth:
            all_word_list.append(word_row_list)
            words_row = words[i]
            word_row_list = [words[i]]
        else:
            words_row += ' ' + words[i]
            word_row_list.append(words[i])


        if i == len(words) - 1:
            all_word_list.append(word_row_list)
    


    # 实现两端对齐
    for i in range(len(all_word_list)):
        words_row_str = ''
        if i == len(all_word_list) - 1:
            for w in all_word_list[i]:
                words_row_str += w + ' '
            words_row_str = words_row_str[:-1]
            words_row_str += ' ' * (maxWidth - len(words_row_str))
            result.append(words_row_str)
        else:
            n_space = len(all_word_list[i]) - 1
            if n_space == 0: 
                words_row_str = all_word_list[i][0] + ' ' * (maxWidth - len(all_word_list[i][0]))
                result.append(words_row_str)
            else:
                n_space_all = maxWidth - sum([len(w) for w in all_word_list[i]])
                n_space_each = n_space_all // n_space
                n_space_left = n_space_all % n_space
                words_row_str = all_word_list[i][0]
                for j in range(1, len(all_word_list[i])):
                    if j <= n_space_left:
                        words_row_str += ' ' * (n_space_each + 1) + all_word_list[i][j]
                    else:
                        words_row_str += ' ' * (n_space_each) + all_word_list[i][j]
                result.append(words_row_str)

           
            
    return result





if __name__ == "__main__":
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # maxWidth = 16
    # words = ["What","must","be","acknowledgment","shall","be"]
    # maxWidth = 16
    # words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    # maxWidth = 20
    words = ["a"]
    maxWidth = 1
    result = fullJustify(words, maxWidth)
    print(result)
        