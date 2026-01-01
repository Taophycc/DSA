class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements except self using explicit arrays.
        
        PATTERN: Prefix & Suffix Arrays (Unoptimized Space)
        TIME COMPLEXITY: O(N) - We iterate through the array three times (Prefix, Suffix, Merge).
        SPACE COMPLEXITY: O(N) - We use two extra arrays 'prefix' and 'suffix' of size N.
        
        STRATEGY:
        1. Initialize two arrays, 'prefix' and 'suffix', with 1s.
        2. Fill the 'prefix' array such that prefix[i] contains the product of all nums to the left of i.
        3. Fill the 'suffix' array such that suffix[i] contains the product of all nums to the right of i.
        4. The final result at index i is simply prefix[i] * suffix[i].
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        # 1. Build Prefix Array (Left to Right)
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        # 2. Build Suffix Array (Right to Left)
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
            
        # 3. Build Result (Multiply them)
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
            
        return res


# Optimized solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements except self without using division.
        
        PATTERN: Prefix & Suffix Products (Space Optimized)
        TIME COMPLEXITY: O(N) - Two passes (one forward, one backward).
        SPACE COMPLEXITY: O(1) - The output array is not counted as extra space; 
                                 we use only one variable 'postfix' for calculation.
        
        STRATEGY:
        1. Create a result array initialized with 1s.
        2. Pass 1 (Prefix): Iterate forward, storing the running product of elements 
           to the LEFT in the result array.
        3. Pass 2 (Suffix): Iterate backward, maintaining a running product of elements 
           to the RIGHT (postfix) variable.
        4. Multiply the stored prefix (in result array) by the current postfix to 
           get the final answer in-place.
        """
        n = len(nums)
        res = [1] * n

        # Pass 1: Calculate Prefix (Left) Products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2: Calculate Postfix (Right) Products & Merge
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
