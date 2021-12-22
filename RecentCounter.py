Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class RecentCounter:

    def __init__(self):
        self.cell = []

    def ping(self, t: int) -> int:
        self.cell.append(t)
        count = 0
        for i in range(len(self.cell)):
            if self.cell[-1]-self.cell[-(1+i)]<=3000:
                count +=1
            else:
                return count
        return count