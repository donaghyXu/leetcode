# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  只会存在一个有效答案 
#  
# 
#  
# 
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 
# 
#  Related Topics 数组 哈希表 👍 18502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 4.内置函数enumerate遍历数组提升速度
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        hash_map = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in hash_map:
                return [i, hash_map[other]]
            hash_map[num] = i

        # 3.融合法2的两次for循环，边存边比
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # hash_map = {}
        # for i in range(len(nums)):
        #     other = target - nums[i]
        #     if other in hash_map:
        #         return [i, hash_map[other]]
        #     hash_map[nums[i]] = i

        # 2.字典模拟哈希表存储，哈希表查找近似为恒定O(1)
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # n = len(nums)
        # hash_map = {}
        # for i in range(n):
        #     hash_map[nums[i]] = i
        #
        # for i in range(n):
        #     other = target - nums[i]
        #     if other in hash_map and hash_map.get(other) != i:
        #         return [i, hash_map.get(other)]

        # 1.双重循环，暴力破解
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
# leetcode submit region end(Prohibit modification and deletion)
