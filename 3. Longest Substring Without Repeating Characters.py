class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        lo = 0
        hi = 0
        
        characters = {}
        
        longest_length = 0
                
        while hi < len(s):
            
            while hi < len(s) and (s[hi] not in characters or characters[s[hi]] == 0):
                
                character = s[hi]
                
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
                    
                hi += 1
            
            curr_length = hi - lo
            
            if curr_length > longest_length:
                longest_length = curr_length
            
            if hi < len(s):
            
                while characters[s[hi]] > 0:
                    characters[s[lo]] -= 1
                    lo +=1
                    
        return longest_length
            
            
