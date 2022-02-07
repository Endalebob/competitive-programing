class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first = 0
        last = len(people)-1
        count = 0
        while first <= last:
            if people[first] + people[last] <= limit:
                first += 1
            last -= 1
            count += 1
        return count