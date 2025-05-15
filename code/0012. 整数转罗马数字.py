def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    thousand = num // 1000
    hundred = num % 1000 // 100
    ten = num % 100 // 10
    one = num % 10
    result = ""
    if one == 4: 
        result += "IV"
    elif one == 9:
        result += "IX"
    elif one >= 5:
        result += "V" + "I" * (one - 5)
    else:
        result += "I" * one
    if ten == 4:
        result = "XL" + result
    elif ten == 9:
        result = "XC" + result
    elif ten >= 5:
        result = "L" + "X" * (ten - 5) + result
    else:
        result = "X" * ten + result
    if hundred == 4:
        result = "CD" + result
    elif hundred == 9:
        result = "CM" + result
    elif hundred >= 5:
        result = "D" + "C" * (hundred - 5) + result
    else:
        result = "C" * hundred + result
    result = "M" * thousand + result
    return result
    



if __name__ == '__main__':
    num = 1994
    result = intToRoman(num)
    print(result)
