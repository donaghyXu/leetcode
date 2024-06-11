# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
# 
#  Related Topics 哈希表 字符串 回溯 👍 2804 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.digit_map = {'2': ['a', 'b', 'c'],
                          '3': ['d', 'e', 'f'],
                          '4': ['g', 'h', 'i'],
                          '5': ['j', 'k', 'l'],
                          '6': ['m', 'n', 'o'],
                          '7': ['p', 'q', 'r', 's'],
                          '8': ['t', 'u', 'v'],
                          '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        # 回溯
        # 时间复杂度：O(3^m * 4^n)，其中m是对应四个字母的数字个数，n是对应三个字母的数字个数
        # 空间复杂度：O(3^m * 4^n)
        digits_len = len(digits)
        if not digits_len:
            return []
        self.back_tracking(digits, 0)
        return self.result

    def back_tracking(self, digits, index):
        if len(self.path) == len(digits):
            self.result.append("".join(self.path))
            return

        digit_key = digits[index]
        digit_list = self.digit_map[digit_key]
        for digit in digit_list:
            self.path.append(digit)
            self.back_tracking(digits, index + 1)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
