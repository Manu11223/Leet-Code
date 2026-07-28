class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largest_rectangle_area(heights: list[int]) -> int:
            stack = []
            area = 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    area = max(area, height * width)
                stack.append(i)
            return area

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largest_rectangle_area(heights))

        return max_area