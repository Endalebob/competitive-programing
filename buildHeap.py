Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    
    def buildHeap(self,arr,n):
        for i in range(n//2-1,-1,-1):
            self.down_heap(i,arr,n)
            
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.down_heap(0,arr,i)
            
    def parent(self,j):
        return (j-1)//2
        
    def left(self,j):
        return (j*2)+1
    
    def right(self,j):
        return (j*2)+2
        
    def down_heap(self,j,arr,n):
        left = self.left(j)
        right = self.right(j)
        original = j
        if left<n:
            if arr[original]<arr[left]:
                original = left
        if right<n:
            if arr[original]<arr[right]:
                original = right
        if original != j:
            arr[original], arr[j] = arr[j],arr[original]
            self.down_heap(original,arr,n)
            