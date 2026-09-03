import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> list of (time, tweetId)
        self.following = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))

        result = []
        while heap and len(result) < 10:
            negT, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)
            if idx > 0:            # <-- must be strictly > 0, not >= 0
                idx -= 1
                t, tid2 = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid2, uid, idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)