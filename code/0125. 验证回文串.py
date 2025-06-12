def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if s == '':
        return True
    
    num_str = len(s)

    p = 0
    q = num_str - 1


    while 1:
        if s[p].isalnum() and s[q].isalnum():
            if s[p].lower() == s[q].lower():
                p += 1
                q -= 1
            else:
                return False
        else:
            if not s[q].isalnum():
                q -= 1
            if not s[p].isalnum():
                p += 1 
        if p >= q:
            break
    return True
    

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    s = " "
    result = isPalindrome(s)
    print(result)