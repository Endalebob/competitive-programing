class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appear =set()
        for i in nums:
            if i in appear:
                return True
            appear.add(i)
        return False