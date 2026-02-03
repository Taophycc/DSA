class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        state = 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
                
            if state == 0: 
                # Check if we start with an upward trend
                if nums[i+1] > nums[i]: 
                    state = 1 
                else:
                    return False #  Started downwards

            elif state == 1: # First Ascent
                if nums[i+1] < nums[i]: 
                    # Found the Peak, Transition to Descent state.
                    state = 2 
            
            elif state == 2: # Descent
                if nums[i+1] > nums[i]: 
                    # Found the Valley, Transition to Second Ascent state.
                    state = 3 
            
            elif state == 3: # Second Ascent
                if nums[i+1] < nums[i]:
                    # Creating a 'W' shape instead of N in a trionic array. Mismatch
                    return False
                    
        return state == 3