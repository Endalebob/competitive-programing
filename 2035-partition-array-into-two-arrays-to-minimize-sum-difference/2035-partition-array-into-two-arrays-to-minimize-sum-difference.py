class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        half_sum = total_sum // 2
        nums_len = len(nums)

        @lru_cache(None)
        def get_options(i, to_pick):
            if not to_pick:
                return [0]
            if i == nums_len:
                return []
            merged_options = heapq.merge(get_options(i + 1, to_pick), [e + nums[i] for e in get_options(i + 1, to_pick - 1)])
            return [k for k, _ in itertools.groupby(merged_options)]

        @lru_cache(None)
        def dynamic_programming(i, to_pick, target):
            if not to_pick:
                return 0
            if i == nums_len:
                return math.inf
            if i < nums_len // 2:
                ans1 = dynamic_programming(i + 1, to_pick, target)
                ans2 = dynamic_programming(i + 1, to_pick - 1, target - nums[i]) + nums[i]
                diff1 = abs(target - ans1)
                diff2 = abs(target - nums[i] - dynamic_programming(i + 1, to_pick - 1, target - nums[i]))
                if diff1 < diff2:
                    return ans1
                elif diff1 == diff2:
                    return max(ans1, ans2)
                else:
                    return ans2
            else:
                options = get_options(i, to_pick)
                index = bisect.bisect(options, target)
                answer = math.inf
                if index < len(options):
                    answer = options[index]
                if index and abs(options[index - 1] - target) < abs(answer - target):
                    answer = options[index - 1]
                return answer

        closest_sum = dynamic_programming(1, nums_len // 2 - 1, half_sum - nums[0]) + nums[0]
        return abs(total_sum - 2 * closest_sum)