Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertionSort1(n, arr):
    count = 1
    for j in range(n-1):
        if arr[-j-1] < arr[-j-2]:
            count +=1
            temp = arr[-j-1]
            arr[-j-1] = arr[-j-2]
            for i in range(n):
                print(arr[i],end=' ')
            print()
            arr[-j-2] = temp
            if count == n:
                for i in range(n):
                    print(arr[i],end=' ')

        else:
            for i in range(n):
                print(arr[i],end=' ')
            return