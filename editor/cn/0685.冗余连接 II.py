# 在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节
# 点没有父节点。 
# 
#  输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条
# 附加的边不属于树中已存在的边。 
# 
#  结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 
# vi 的一个父节点。 
# 
#  返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：edges = [[1,2],[1,3],[2,3]]
# 输出：[2,3]
#  
# 
#  示例 2： 
#  
#  
# 输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# 输出：[4,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == edges.length 
#  3 <= n <= 1000 
#  edges[i].length == 2 
#  1 <= ui, vi <= n 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 405 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.father = [i for i in range(1005)]

    def find(self, u):
        if u == self.father[u]:
            return u
        else:
            self.father[u] = self.find(self.father[u])
            return self.father[u]

    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.father[v] = u

    def is_tree_after_remove_edge(self, edges, edge):
        for i in range(len(edges)):
            if i == edge:
                continue
            if self.is_same(edges[i][0], edges[i][1]):
                return False
            self.join(edges[i][0], edges[i][1])
        return True

    def get_redundant_edge(self, edges):
        self.__init__()
        for edge in edges:
            if self.is_same(edge[0], edge[1]):
                return edge
            else:
                self.join(edge[0], edge[1])
        return []

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        n = len(edges)
        indegree = [0] * (n + 1)
        for edge in edges:
            indegree[edge[1]] += 1

        res = []
        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 2:
                res.append(i)

        # 如果有入度为2的
        if len(res) > 0:
            if self.is_tree_after_remove_edge(edges, res[0]):
                return edges[res[0]]
            else:
                return edges[res[1]]

        # 没有入度为2的，判断哪里有环
        return self.get_redundant_edge(edges)
# leetcode submit region end(Prohibit modification and deletion)
