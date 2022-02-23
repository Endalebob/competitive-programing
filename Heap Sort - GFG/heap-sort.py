#User function Template for python3

class Solution:
    
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
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends