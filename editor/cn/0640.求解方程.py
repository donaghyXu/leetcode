# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。 
# 
#  如果方程没有解或存在的解不为整数，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。 
# 
#  题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
#  
# 
#  示例 2: 
# 
#  
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
#  
# 
#  示例 3: 
# 
#  
# 输入: equation = "2x=x"
# 输出: "x=0"
#  
# 
#  
# 
#  提示: 
# 
#  
#  3 <= equation.length <= 1000 
#  equation 只有一个 '='. 
#  方程由绝对值在 [0, 100] 范围内且无任何前导零的整数和变量 'x' 组成。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 212 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveEquation(self, equation: str) -> str:
        eq_split = equation.split("=")
        a = eq_split[0]
        b = eq_split[1]

        # import pdb
        # pdb.set_trace()
        if "+" in a or "-" in a:
            a_split = a.replace("-", "+-").split("+")
        else:
            a_split = [a]
        x_pre = 0
        num_pre = 0
        # import pdb
        # pdb.set_trace()
        for item in a_split:
            if item == "":
                continue
            if "x" in item:
                if len(item) == 1:
                    x_pre += 1
                elif len(item) == 2 and "-" in item:
                    x_pre -= 1
                else:
                    x_pre += int(item.replace("x", ""))
            else:
                num_pre += int(item)

        if "+" in b or "-" in b:
            b_split = b.replace("-", "+-").split("+")
        else:
            b_split = [b]
        x_right_pre = 0
        num_right_pre = 0
        for item in b_split:
            if item == "":
                continue
            if "x" in item:
                if len(item) == 1:
                    x_right_pre += 1
                elif len(item) == 2 and "-" in item:
                    x_right_pre -= 1
                else:
                    x_right_pre += int(item.replace("x", ""))
            else:
                num_right_pre += int(item)

        x_final_pre = x_pre - x_right_pre
        num_final_pre = num_right_pre - num_pre
        if x_final_pre == 0 and num_final_pre == 0:
            return "Infinite solutions"
        elif x_final_pre == 0 and num_final_pre != 0:
            return "No solution"
        else:
            return "x=%d" % (num_final_pre // x_final_pre)
# leetcode submit region end(Prohibit modification and deletion)
