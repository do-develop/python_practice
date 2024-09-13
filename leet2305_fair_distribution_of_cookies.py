class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        N = len(cookies)
        INF = 10**9  # Large integer to represent infinity

        def dfs(i, zero_count):
            # If the remaining cookies can't fill all empty slots, return a large number
            if zero_count > N - i:
                return INF
            
            # If all cookies are distributed, return the maximum cookies received by any child
            if i == N:
                return max(distribution)
            
            # Initialize the answer to a large number
            answer = INF
            
            # Try giving the current cookie to each child
            for j in range(k):
                # Check if we're filling an empty slot
                was_zero = distribution[j] == 0
                
                # Add the i-th cookie to child j
                distribution[j] += cookies[i]
                
                # If it was zero before, decrement the zero count
                answer = min(answer, dfs(i + 1, zero_count - was_zero))
                
                # Undo the addition (backtrack)
                distribution[j] -= cookies[i]
                
                # If the distribution for this child is zero after backtracking, increment the zero count back
                if was_zero and distribution[j] == 0:
                    zero_count += 1
            
            return answer

        return dfs(0, k)
