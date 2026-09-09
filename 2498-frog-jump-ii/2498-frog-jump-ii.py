class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        def check(cap):
            visited = set()
            curr_index = 0

            while curr_index < n - 1:
                next_index = curr_index

                while next_index + 1 < n and stones[next_index + 1] - stones[curr_index] <= cap:
                    next_index += 1

                if curr_index == next_index:
                    return False

                visited.add(next_index)
                curr_index = next_index
            
            return_path = [0]
            for i in range(1, n):
                if i not in visited:
                    return_path.append(stones[i])
            return_path.append(stones[-1])

            return_path.sort()

            for i in range(1, len(return_path)):
                if return_path[i] - return_path[i-1] > cap:
                    return False
            
            return True
        
        low = 1
        high = stones[-1] - stones[0]
        best_answer = high
        
        while low <= high:
            mid_guess = (low + high) // 2
            
            if check(mid_guess):
                best_answer = mid_guess
                high = mid_guess - 1
            else:
                low = mid_guess + 1
                
        return best_answer
            


