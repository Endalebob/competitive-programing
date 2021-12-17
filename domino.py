Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def domino(r,c):
    if r%2==0:
        return c * (r//2)
    else:
        return c * (r//2) + (c//2)
 
tc = input().split()
row, col = int(tc[0]), int(tc[1])
print(domino(row, col))