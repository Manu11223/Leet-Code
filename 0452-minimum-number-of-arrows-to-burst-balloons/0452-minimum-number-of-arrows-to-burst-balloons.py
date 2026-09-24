class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            if start > arrow_pos:  # doesn't overlap current arrow
                arrows += 1
                arrow_pos = end
            # else: this balloon is already burst by arrow_pos, do nothing

        return arrows