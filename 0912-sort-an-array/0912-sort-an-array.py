class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(collection):
            def merge(left: list, right: list) -> list:
                
                def _merge():
                    while left and right:
                        yield (left if left[0] <= right[0] else right).pop(0)
                    yield from left
                    yield from right

                return list(_merge())

            if len(collection) <= 1:
                return collection
            mid = len(collection) // 2
            return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))
        return merge_sort(nums)
