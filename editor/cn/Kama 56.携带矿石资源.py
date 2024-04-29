class Solution:
    def solve(self, c, n, weights, prices, amounts):
        # 动态规划
        # 时间复杂度：O(sum(amounts)*c)
        # 空间复杂度：O(c)
        
        # 转换为0-1背包
        new_n = sum(amounts)
        weights_new = [0] * new_n
        prices_new = [0] * new_n
        
        index = 0
        for i in range(n):
            amount_num = amounts[i]
            for j in range(amount_num):
                weights_new[index] = weights[i]
                prices_new[index] = prices[i]
                index += 1
        
        #dp[j]:容量为j的背包最大能放矿石的总价值
        dp = [0] * (c + 1)
        
        # 递推，遍历
        for i in range(new_n):
            for j in range(c, weights_new[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weights_new[i]] + prices_new[i])
        return dp[c]
    

if __name__ == "__main__":
    line = [int(x) for x in input().split()]
    c = line[0]
    n = line[1]
    
    weights = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split()]
    amounts = [int(x) for x in input().split()]
    s = Solution()
    print(s.solve(c, n, weights, prices, amounts))