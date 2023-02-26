class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        # Sort the input list in ascending order
        nums.sort()
        
        # Set the upper bound of the search range to the index of the middle element
        hi = (len(nums) - 1) // 2 + 1
        
        # Set the initial index for searching to the last element of the list
        r = len(nums) - 1
        
        # Initialize a variable to keep track of the number of marked indices
        ans = 0
        
        # Keep searching for marked indices while there is still a valid search space
        while hi > 0 and r >= (len(nums) - 1) // 2 + 1:
            # Calculate the threshold value for the current search iteration
            num = nums[r] // 2
            
            # Find the index of the first element greater than the threshold
            # in the search range
            idx = bisect_right(nums, num, lo=0, hi=hi)
            
            # If such an element exists, mark it and the middle element
            if idx > 0:
                ans += 2
                
                # Update the upper bound of the search range to the left of the marked elements
                hi = idx - 1
            
            # If no such element exists, stop searching
            else:
                break
            
            # Move to the next element to the left for the next iteration
            r -= 1
        
        # Return the maximum number of marked indices found
        return ans
