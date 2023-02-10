class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        valid_index1 = [(i, j) for i, row in enumerate(img1) for j, num in enumerate(row) if num]
        valid_index2 = [(i, j) for i, row in enumerate(img2) for j, num in enumerate(row) if num]
        indexCounter = collections.Counter((i - x, j - y) for i, j in valid_index1 for x, y in valid_index2)
        return 0 if not indexCounter else max(indexCounter.values())
