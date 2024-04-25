class Solution:
    def solve(self, n, v, wi, vi):
        # dp[j]:容量为j的背包所能携带的最大价值
        dp = [0] * (v + 1)
        
        # 递推 循环
        for i in range(n):
            for j in range(wi[i], v + 1):
                dp[j] = max(dp[j], dp[j - wi[i]] + vi[i])
        return dp[v]
    
    
if __name__ == "__main__":
    first_line = [int(x) for x in input().split()]
    n = first_line[0]
    v = first_line[1]
    wi = [0] * n
    vi = [0] * n
    for i in range(n):
        line = [int(x) for x in input().split()]
        wi[i] = line[0]
        vi[i] = line[1]
    s = Solution()
    print(s.solve(n, v, wi, vi))