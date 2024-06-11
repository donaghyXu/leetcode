# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序） 
# 
#  
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：graph = [[1,2],[3],[3],[]]
# 输出：[[0,1,3],[0,2,3]]
# 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
# 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == graph.length 
#  2 <= n <= 15 
#  0 <= graph[i][j] < n 
#  graph[i][j] != i（即不存在自环） 
#  graph[i] 中的所有元素 互不相同 
#  保证输入为 有向无环图（DAG） 
#  
# 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 回溯 👍 478 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n²)
        self.path.append(0)
        self.back_tracking(graph, 0)
        return self.res

    def back_tracking(self, graph, start_index):
        n = len(graph)
        if start_index == n - 1:
            # list可变，必须用deepcopy
            self.res.append(self.path[:])
            return

        next_index_list = graph[start_index]
        for next_index in next_index_list:
            self.path.append(next_index)
            self.back_tracking(graph, next_index)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
