Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def countingSort(arr):
    new_arr = 100*[0]
    for i in arr:
        new_arr[i] += 1
    return new_arr