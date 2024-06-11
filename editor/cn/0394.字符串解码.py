# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 30 
#  
#  s 由小写英文字母、数字和方括号
#  '[]' 组成 
#  s 保证是一个 有效 的输入。 
#  s 中所有整数的取值范围为
#  [1, 300] 
#  
# 
#  Related Topics 栈 递归 字符串 👍 1768 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        # 栈
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n)
        stack = []
        for element in s:
            if element == "]":
                sub_s = []
                while stack[-1] != "[":
                    sub_s.append(stack.pop())
                stack.pop()

                num_list = []
                while stack and stack[-1].isdigit():
                    num_list.append(stack.pop())
                num = "".join(num_list[::-1])

                for i in range(int(num)):
                    for j in range(len(sub_s) - 1, -1, -1):
                        stack.append(sub_s[j])
            else:
                stack.append(element)
        return "".join(stack)
# leetcode submit region end(Prohibit modification and deletion)
