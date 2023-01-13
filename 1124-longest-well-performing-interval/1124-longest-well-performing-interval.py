from collections import defaultdict
class Solution:
    def longestWPI(self, nums: List[int]) -> int:
        # i was wrong in the first attempt it’s amazing I’m sure if this is the will of God I will pass even if they ask me segment tree with lazy propagation if it is not it is better not to pass wow uuuuuuu…. Yes

        '''
        Calculate the current score.
        '''
        _track = defaultdict(int)
        _score = 0
        ans = 0
        for i in range(len(nums)):
            _score = _score + 1 if nums[i] > 8 else _score - 1
            if _score > 0:
                ans = i+1
            if _score not in _track:
                _track[_score] = i
            if _score - 1 in _track:
                ans = max(ans,i-_track[_score-1])
        return ans
