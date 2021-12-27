Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        cal = []
        ans = []
        for i in points:
            dis = i[0]**2 + i[1]**2
            if dis not in dic:
                dic[dis] = [i]
            else:
                dic[dis].append(i)
            cal.append(dis)
        cal.sort()
        for i in range(k):
            while len(dic[cal[i]])>0:
                ans.append(dic[cal[i]].pop())
        return ans