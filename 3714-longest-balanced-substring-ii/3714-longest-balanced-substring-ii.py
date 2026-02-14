class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        current_run = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                current_run += 1
            else:
                current_run = 1
            max_len = max(max_len, current_run)

        def solve_two(c1, c2, forbidden):
            local_max = 0
            diff = 0
            seen = {0: -1} 
            
            for i, char in enumerate(s):
                if char == forbidden:
                    seen = {0: i}
                    diff = 0
                else:
                    if char == c1:
                        diff += 1
                    else: 
                        diff -= 1
                    
                    if diff in seen:
                        local_max = max(local_max, i - seen[diff])
                    else:
                        seen[diff] = i
            return local_max

        max_len = max(max_len, solve_two('a', 'b', 'c'))
        max_len = max(max_len, solve_two('a', 'c', 'b'))
        max_len = max(max_len, solve_two('b', 'c', 'a'))

        def solve_three():
            local_max = 0
            a = b = c = 0
            seen = {(0, 0): -1}
            
            for i, char in enumerate(s):
                if char == 'a': a += 1
                elif char == 'b': b += 1
                elif char == 'c': c += 1
                
                state = (a - b, b - c)
                
                if state in seen:
                    local_max = max(local_max, i - seen[state])
                else:
                    seen[state] = i
            return local_max

        max_len = max(max_len, solve_three())
        
        return max_len