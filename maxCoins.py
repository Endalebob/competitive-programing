Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        summ = 0
        print(piles)
        for i in range(len(piles)//3):
            summ += piles[(-2*i-2)]
        return summ