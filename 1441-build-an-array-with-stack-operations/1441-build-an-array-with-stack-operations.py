class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # [1]
        ptr = 0
        stack = []
        ans = []
        for i in range(1,n+1):
            if stack and len(stack) > ptr:
                ans.append("Pop")
                stack.pop()
            stack.append(i)
            ans.append("Push")
            ptr += (stack[-1]==target[ptr])
            if ptr == len(target):
                return ans
        return ans