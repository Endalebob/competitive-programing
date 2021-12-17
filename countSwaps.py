Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def countSwaps(a):
    count = 0
    for i in range(len(a)):
        
        for j in range(len(a)-1):
            
            if a[j] > a[j+1]:
                count+=1
                a[j+1], a[j] = a[j], a[j+1]  
    print('Array is sorted in',count, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
    return count, a