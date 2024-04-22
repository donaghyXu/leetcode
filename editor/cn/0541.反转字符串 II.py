# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由小写英文组成 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics 双指针 字符串 👍 591 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 1.模拟
        # 时间复杂度：O(nk)
        # 空间复杂度：O(n)
        res = list(s)
        cnt = int(len(s) / (2 * k))
        for i in range(cnt):
            res[i * 2 * k: (i * 2 + 1) * k] = reversed(res[i * 2 * k: (i * 2 + 1) * k])
        left = len(s) - cnt * (2 * k)
        if left < k:
            res[cnt * 2 * k:] = reversed(res[cnt * 2 * k:])
        else:
            res[cnt * 2 * k: (cnt * 2 + 1) * k] = reversed(res[cnt * 2 * k: (cnt * 2 + 1) * k])
        return ''.join(res)
# leetcode submit region end(Prohibit modification and deletion)
