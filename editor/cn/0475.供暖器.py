# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。 
# 
#  在加热器的加热半径范围内的每个房屋都可以获得供暖。 
# 
#  现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。 
# 
#  注意：所有供暖器 heaters 都遵循你的半径标准，加热的半径也一样。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
#  
# 
#  示例 2: 
# 
#  
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。
#  
# 
#  示例 3： 
# 
#  
# 输入：houses = [1,5], heaters = [2]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= houses.length, heaters.length <= 3 * 10⁴ 
#  1 <= houses[i], heaters[i] <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 二分查找 排序 👍 474 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 双指针
        # 时间复杂度：O(logn * len(houses) * len(heaters)
        # 空间复杂度：O(1)
        max_house = max(houses)
        max_heater = max(heaters)
        houses.sort()
        heaters.sort()
        left = 0
        right = max(max_house, max_heater)
        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(houses, heaters, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def valid(self, houses, heaters, r):
        cnt = 0
        index = 0
        total = len(houses)
        for heater in heaters:
            left_cover = heater - r
            right_cover = heater + r
            while cnt < total and \
                    left_cover <= houses[index] <= right_cover:
                index += 1
                cnt += 1
            if cnt == total:
                return True
        return False




# leetcode submit region end(Prohibit modification and deletion)
