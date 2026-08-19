import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Events: (x, -height, right) for start, (x, 0, right) for end marker isn't quite enough;
        # use: start -> (left, -height, right); end -> (right, 0, right) as a sentinel to trigger cleanup
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))   # start: negative height sorts taller first
            events.append((right, 0, right))          # end marker (height=0 sorts after starts at same x)
        
        events.sort()
        
        result = []
        # max-heap of (-height, end_x); heap[0] is current tallest active building
        live = [(0, float('inf'))]  # sentinel: ground level, never expires
        
        for x, neg_h, right in events:
            if neg_h < 0:
                # It's a start event: push the building
                heapq.heappush(live, (neg_h, right))
            
            # Lazy deletion: pop any buildings from top that have already ended by x
            while live[0][1] <= x:
                heapq.heappop(live)
            
            current_height = -live[0][0]
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])
        
        return result