# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。 
# 
# 
#  所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。 
# 
# 
#  
#  例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。 
#  
# 
#  假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
#  
# 
#  示例 2： 
#  
#  
# 输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL",
# "SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tickets.length <= 300 
#  tickets[i].length == 2 
#  fromi.length == 3 
#  toi.length == 3 
#  fromi 和 toi 由大写英文字母组成 
#  fromi != toi 
#  
# 
#  Related Topics 深度优先搜索 图 欧拉回路 👍 906 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.targets = {}
        self.result = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 回溯
        # 时间复杂度：
        # 空间复杂度：
        tickets.sort(key=lambda x: x[1])
        for ticket in tickets:
            if ticket[0] in self.targets:
                if ticket[1] in self.targets[ticket[0]]:
                    self.targets[ticket[0]][ticket[1]] += 1
                else:
                    self.targets[ticket[0]][ticket[1]] = 1
            else:
                self.targets[ticket[0]] = {ticket[1]: 1}
        self.result.append("JFK")
        self.back_tracking(len(tickets))
        return self.result

    def back_tracking(self, ticket_num):
        if len(self.result) == (ticket_num + 1):
            return True

        targets_key = self.result[len(self.result) - 1]
        if targets_key in self.targets:
            target_dict = self.targets[targets_key]
            for target_key in target_dict.keys():
                if target_dict[target_key] > 0:
                    self.result.append(target_key)
                    target_dict[target_key] -= 1
                    if self.back_tracking(ticket_num):
                        return True
                    self.result.pop()
                    target_dict[target_key] += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
