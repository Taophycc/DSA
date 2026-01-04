class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            # Calculate integer square root. 
            # We only need to search up to sqrt(num) because divisors come in pairs.
            sqrt = int(num**0.5)
            curr_sum = 0
            cnt = 0
            
            for i in range(1, sqrt + 1):
                # 1. Check if 'i' is a divisor
                if num % i == 0:
                    cnt += 1
                    curr_sum += i
                    
                    # 2. Add the corresponding pair (quotient)
                    # Example: If num=21 and i=3, the pair is 7 (21 // 3).
                    # We check 'i != num // i' to avoid double-counting perfect squares (like 5*5=25)
                    if i != (num // i):
                        cnt += 1
                        curr_sum += (num // i)
                
                # 3. Optimization: Early Exit
                # If we have already found more than 4 divisors, this number is invalid.
                # Break the loop immediately to save time.
                if cnt > 4:
                    break
            
            # 4. Final Check
            # Only add to the total if we found EXACTLY 4 divisors.
            if cnt == 4:
                total_sum += curr_sum
        
        return total_sum