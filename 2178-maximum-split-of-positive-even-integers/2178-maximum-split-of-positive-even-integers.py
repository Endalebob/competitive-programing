class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        used_numbers = []
        current_sum = 0
        i = 1
        while current_sum<=finalSum:
            used_numbers.append(i*2)
            current_sum += i*2
            i += 1
        used_numbers.pop((current_sum-finalSum)//2 - 1)
        return used_numbers