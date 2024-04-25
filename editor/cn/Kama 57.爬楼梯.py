class Solution:
    def solve(self, n, m):
        # 动态规划
        # 时间复杂度：O(mn)
        # 空间复杂度：O(n)
        
        # dp[j]: 爬到j阶梯有多少种不同的方法
        dp = [0] * (n + 1)
        
        # 初始化
        dp[0] = 1
        
        # 递推，遍历，排列
        for i in range(n+1):
            for j in range(1, m+1):
                dp[i] += dp[i - j]
        return dp[n]
                
    
if __name__ == "__main__":
    line = [int(x) for x in input().split()]
    n = line[0]
    m = line[1]
    s = Solution()
    print(s.solve(n, m))