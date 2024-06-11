class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        # 模拟
        # 时间复杂度：O(mn)
        # 空间复杂度：O(mn)
        m = len(array)
        if m == 0:
            return []
        n = len(array[0])

        min_num = min(m, n)
        # 循环圈数
        loop = int(min_num / 2)
        # 循环不变量的偏移量
        offset = 1
        # 起始坐标
        x_start = 0
        y_start = 0

        result = []
        while loop:
            # 计算上方行
            y_end = y_start + n - offset
            for i in range(y_start, y_end):
                result.append(array[x_start][i])

            # 计算右侧列
            x_end = x_start + m - offset
            for i in range(x_start, x_end):
                result.append(array[i][y_end])

            # 计算下方行
            for i in range(y_end, y_start, -1):
                result.append(array[x_end][i])

            # 计算左侧列
            for i in range(x_end, x_start, -1):
                result.append(array[i][y_start])

            loop -= 1
            x_start += 1
            y_start += 1
            offset += 2

        # 根据最小行或列的奇偶情况，计算中心位置落单的行或列
        if min_num % 2:
            if m < n:
                for i in range(y_start, y_start + n - offset + 1):
                    result.append(array[x_start][i])
            else:
                for i in range(x_start, x_start + m - offset + 1):
                    result.append(array[i][y_start])
        return result
# runtime:36 ms
# memory:17.1 MB
