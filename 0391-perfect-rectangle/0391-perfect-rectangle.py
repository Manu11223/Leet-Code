class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        total_area = 0

        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')

        for x1, y1, x2, y2 in rectangles:
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)

            total_area += (x2 - x1) * (y2 - y1)

            for corner in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        if corners != expected_corners:
            return False

        return total_area == (max_x - min_x) * (max_y - min_y)