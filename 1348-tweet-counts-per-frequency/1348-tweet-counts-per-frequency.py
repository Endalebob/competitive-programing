class TweetCounts:

    def __init__(self):
        self.mp = {"minute":60,"hour":3600,"day":86400}
        self.record = defaultdict(dict)
        
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if time in self.record[tweetName]:
            self.record[tweetName][time] += 1
        else:
            self.record[tweetName][time] = 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        def find():
            ans = []
            max_ = endTime
            for i in range(startTime,max_+1,self.mp[freq]):
                temp = 0
                for c in range(i,min(i+self.mp[freq],max_+1)):
                    if c in self.record[tweetName]:
                        temp += self.record[tweetName][c]
                ans.append(temp)
            return ans
        return find()
        
                    
                       


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)