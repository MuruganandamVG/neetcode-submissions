import heapq
class Twitter:

    def __init__(self):
        self.tweets={}
        self.followlist={}
        self.time=0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.time+=1
        self.tweets[userId].append((-self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds=[]
        feeds.extend(self.tweets.get(userId,[]))
        followerlist=[]
        if userId in self.followlist:
            followerlist=self.followlist[userId]
        for i in range(len(followerlist)):
            feeds.extend(self.tweets.get(followerlist[i],[]))
        heapq.heapify(feeds)
        recentFeeds=[]
        for i in range(min(len(feeds),10)):
            recentFeeds.append(heapq.heappop(feeds)[1])
        return recentFeeds


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return 
        if followerId not in self.followlist:
            self.followlist[followerId]=[]
        if followeeId not in self.followlist[followerId]:
            self.followlist[followerId].append(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followlist:
            if followeeId in self.followlist[followerId]:
                self.followlist[followerId].remove(followeeId)

        
