# brute force solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxstr = ""
        currstr = ""
        for ch in s:
            if ch not in currstr:
                currstr += ch
            else:
                idx = currstr.index(ch)
                currstr = currstr[idx+1:] + ch
                
            if len(currstr) > len(maxstr):
                maxstr = currstr
        
        return len(maxstr)
    
    
# using two pointers and hash map
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxstrlen = 0
        leftptr = 0
        
        char_idx = dict()
        for rightptr, ch in enumerate(s):
            if ch in char_idx and char_idx[ch] >= leftptr:
                leftptr = char_idx[ch]+1
            char_idx[ch] = rightptr
                
            currlen = rightptr - leftptr + 1
            if currlen > maxstrlen:
                maxstrlen = currlen
        
        return maxstrlen
            