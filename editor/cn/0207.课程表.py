# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。 
# 
#  在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表
# 示如果要学习课程 ai 则 必须 先学习课程 bi 。 
# 
#  
#  例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。 
#  
# 
#  请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。 
# 
#  示例 2： 
# 
#  
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= 5000 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  prerequisites[i] 中的所有课程对 互不相同 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 1963 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 拓扑排序
        # 时间复杂度：O(len(numCourses)+len(prerequisites))
        # 空间复杂度：O(len(numCourses)+len(prerequisites))
        # 思路：从入度为0的节点开始，利用拓扑排序不断往前搜索
        #      如果访问的节点总数等于课程数，那么代表可以修完

        edges = collections.defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            indegree[edge[0]] += 1
            edges[edge[1]].append(edge[0])

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for next_node in edges[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        return visited == numCourses
# leetcode submit region end(Prohibit modification and deletion)
