# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。 
# 
#  注意：如果对空文本输入退格字符，文本继续为空。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ab#c", t = "ad#c"
# 输出：true
# 解释：s 和 t 都会变成 "ac"。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "ab##", t = "c#d#"
# 输出：true
# 解释：s 和 t 都会变成 ""。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a#c", t = "b"
# 输出：false
# 解释：s 会变成 "c"，但 t 仍然是 "b"。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 200 
#  s 和 t 只含有小写字母以及字符 '#' 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？ 
#  
# 
#  Related Topics 栈 双指针 字符串 模拟 👍 728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # # 栈
        # s_res = []
        # t_res = []
        # for i in range(len(s)):
        #     if s[i] != '#':
        #         s_res.append(s[i])
        #     else:
        #         if len(s_res) != 0:
        #             s_res.pop()
        #
        # for i in range(len(t)):
        #     if t[i] != '#':
        #         t_res.append(t[i])
        #     else:
        #         if len(t_res) != 0:
        #             t_res.pop()
        # if s_res == t_res:
        #     return True
        # else:
        #     return False

        # 双指针
        s_list = list(s)
        t_list = list(t)
        s_left = 0
        s_right = 0
        while s_right < len(s_list):
            if s_list[s_right] != '#':
                s_list[s_left] = s_list[s_right]
                s_left += 1
            elif s_list[s_right] == '#' and s_left != 0:
                s_left -= 1
            s_right += 1

        t_left = 0
        t_right = 0
        while t_right < len(t_list):
            if t_list[t_right] != '#':
                t_list[t_left] = t_list[t_right]
                t_left += 1
            elif t_list[t_right] == '#' and t_left != 0:
                t_left -= 1
            t_right += 1
        if s_list[:s_left] == t_list[:t_left]:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
