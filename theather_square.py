Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def theather_square(m, n, a):
    if m % a == 0:
        c = m//a
    else:
        c = m//a + 1
    if n % a == 0:
        r = n//a
    else:
        r = n//a + 1
    return (r * c)
g = input().split()
M,N,A= int(g[0]),int(g[1]),int(g[2])
print(theather_square(M,N,A))