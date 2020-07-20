class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # using hash maps
        counts = dict()
        answer = ""
        for ch in T:
            if ch in S:
                if ch not in counts:
                    counts[ch] = 1
                else:
                    counts[ch] += 1
            else:
                answer += ch
        
        for ch in S:
            if ch in counts:
                count = counts[ch]
                while count:
                    answer += ch
                    count -= 1
                del counts[ch]
        
        return answer


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # using priority queues
        # space O(n+m) | time O(n)
        import heapq
    
        chars = dict()
        for ind, ch in enumerate(S): # O(m)
            chars[ch] = ind
        
        indices, answer = [], ""     # indices - O(log n) time complexity | O(n) space complexity
        for ch in T:                 # O(n)
            if ch in chars:
                heapq.heappush(indices, (chars[ch], ch))
            else:
                answer += ch
        
        while indices:
            answer += heapq.heappop(indices)[1]
        return answer
    
    