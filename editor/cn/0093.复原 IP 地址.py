# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 
# 和 "192.168@1.1" 是 无效 IP 地址。 
#  
# 
#  给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新
# 排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅由数字组成 
#  
# 
#  Related Topics 字符串 回溯 👍 1410 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 回溯
        # 时间复杂度：O(3^4)
        # 空间复杂度：O(n)
        self.back_tracking(s, 0)
        return self.result

    def back_tracking(self, s, start_index):
        # 终止条件
        if len(self.path) == 4 and start_index == len(s):
            self.result.append(".".join(self.path[:]))

        for i in range(start_index, len(s)):
            sub_s = s[start_index:i+1]
            # 剪枝
            if len(self.path) >= 5:
                break
            if self.is_valid(sub_s):
                self.path.append(sub_s)
                self.back_tracking(s, i + 1)
                self.path.pop()

    def is_valid(self, s):
        if len(s) >= 2 and s[0] == "0":
            return False
        if 0 <= int(s) <= 255:
            return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
