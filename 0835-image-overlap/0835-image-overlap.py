class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1ValidIndex = [(i, j) for i, row in enumerate(img1) for j, num in enumerate(row) if num]
        img2ValidIndex = [(i, j) for i, row in enumerate(img2) for j, num in enumerate(row) if num]
        indexCounter = collections.Counter((i - x, j - y) for i, j in img1ValidIndex for x, y in img2ValidIndex)
        return 0 if not indexCounter else max(indexCounter.values())
