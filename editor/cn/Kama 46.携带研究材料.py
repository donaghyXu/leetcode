class Solution:
    def solve(self, m, n, weights, values):
        # 动态规划 一维滚动数组
        # 时间复杂度：O(mn)
        # 空间复杂度：O(n)
        
        # dp[j] 为0-i的物品放到空间为j的背包里的最大价值
        dp = [0 for _ in range(n+1)]
        
        # 上面已初始化
                
        # 递推公式 遍历
        for i in range(m):
            for j in range(n, weights[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weights[i]]+values[i])
        return dp[n]
        
        # # 动态规划 二维数组
        # # 时间复杂度：O(mn)
        # # 空间复杂度：O(mn)
        
        # # dp[i][j] 为0-i的物品放到空间为j的背包里的最大价值
        # dp = [[0 for _ in range(n+1)] for _ in range(m)]
        
        # # 初始化
        # for i in range(n+1):
        #     if i >= weights[0]:
        #         dp[0][i] = values[0]
                
        # # 递推公式 遍历
        # for i in range(1, m):
        #     for j in range(1, n+1):
        #         if j < weights[i]: 
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
        # return dp[m-1][n]
    
if __name__ == "__main__":
    s = Solution()
    first_line = [int(x) for x in input().split()]
    m = first_line[0]
    n = first_line[1]
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    print(s.solve(m, n, weights, values))