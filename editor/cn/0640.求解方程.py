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
        # 模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        left, right = equation.replace("-", "+-").split("=")
        left_list = left.split("+")
        right_list = right.split("+")
        x_pre_suffix = 0
        num_pre_suffix = 0
        for element in left_list:
            if element:
                if element[-1] == "x":
                    if len(element) == 1:
                        x_pre_suffix += 1
                    elif len(element) == 2 and element[0] == "-":
                        x_pre_suffix -= 1
                    else:
                        x_pre_suffix += int(element[:-1])
                else:
                    num_pre_suffix += int(element)

        for element in right_list:
            if element:
                if element[-1] == "x":
                    if len(element) == 1:
                        x_pre_suffix -= 1
                    elif len(element) == 2 and element[0] == "-":
                        x_pre_suffix += 1
                    else:
                        x_pre_suffix -= int(element[:-1])
                else:
                    num_pre_suffix -= int(element)

        if x_pre_suffix == 0 and num_pre_suffix == 0:
            return "Infinite solutions"
        elif x_pre_suffix == 0 and num_pre_suffix != 0:
            return "No solution"
        else:
            return "x={}".format(-int(num_pre_suffix / x_pre_suffix))
# leetcode submit region end(Prohibit modification and deletion)
