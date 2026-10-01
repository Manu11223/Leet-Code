class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        j = 0
        k = len(heaters)
        ans = 0

        for h in houses:
            # advance while the next heater is at least as close
            while j + 1 < k and abs(heaters[j + 1] - h) <= abs(heaters[j] - h):
                j += 1
            d = abs(heaters[j] - h)
            if d > ans:
                ans = d

        return ans