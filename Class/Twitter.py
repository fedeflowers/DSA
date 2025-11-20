# Twitter

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_follows = defaultdict(set)  # userId -> set of followees
        self.user_tweets = defaultdict(Deque)  # userId -> list of (timestamp, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        if len(self.user_tweets[userId]) > 10:
            self.user_tweets[userId].popleft()
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []

        self.user_follows[userId].add(userId)  # Ensure user follows themselves

        for followeeId in self.user_follows[userId]:
            tweets.extend(list(self.user_tweets[followeeId]))  # Only last 10 tweets from each user

        # Get 10 most recent tweets using max-heap (via negating timestamps)
        most_recent = heapq.nlargest(10, tweets, key=lambda x: x[0])
        return [tweetId for _, tweetId in most_recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].discard(followeeId)


#BEST
# merge the lists of followers one tweet at time until 10 tweets
import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.user_follows = defaultdict(set)
        self.user_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Push tweets in reverse chronological order
        self.user_tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_follows[userId].add(userId)
        heap = []

        for followeeId in self.user_follows[userId]:
            tweets = self.user_tweets[followeeId]
            if tweets:
                # (timestamp, tweetId, userId, index in tweet list)
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(heap, (time, tweetId, followeeId, idx))

        result = []
        while heap and len(result) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx > 0:
                next_time, next_tid = self.user_tweets[uid][idx - 1]
                heapq.heappush(heap, (next_time, next_tid, uid, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].discard(followeeId)
