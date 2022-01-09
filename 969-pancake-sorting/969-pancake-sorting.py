class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sorted_list = []
        l = len(arr)
        for i in range (len(arr)):
            ma = max(arr[:l-i])
            if ma == arr[:l-i][-1]:
                continue
            else:
                ind = arr[:l-i].index(ma)
                arr[:ind+1] = arr[:ind+1][::-1]
                sorted_list.append(ind+1)
                arr[:l-i] = arr[:l-i][::-1]
                sorted_list.append(l-i)
        return sorted_list
            