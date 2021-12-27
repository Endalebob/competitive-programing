Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in intervals:
            if len(ans)==0 or i[0] > ans[-1][1]:
                ans.append(i)
            else:
                if i[1]>ans[-1][1]:
                    ans[-1][1] = i[1]       
        return ans