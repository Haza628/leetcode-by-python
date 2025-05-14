# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """ 
    
    p = len(gas) - 1
    left_gas = 0
    cost_gas = 0
    for i in range(len(gas)):
        left_gas += gas[i] - cost[i]
        while 1:
            if left_gas < 0 and p != i:             
                borrow = gas[p] - cost[p]
                left_gas += borrow
                p -= 1
            elif left_gas < 0 and p == i:
                return -1
            else:
                break
        if p == i:
            if p == len(gas) - 1:
                return 0
            else:
                return p + 1


if __name__ == "__main__":
    gas = [3, 1, 1]
    # [1,2,3,4,5] [2,3,4] [6,1,4,3,5]
    cost = [1, 2 ,2] 
    # [3,4,5,1,2] [3,4,3] [3,8,2,4,2]
    result = canCompleteCircuit(gas, cost)
    print(result)