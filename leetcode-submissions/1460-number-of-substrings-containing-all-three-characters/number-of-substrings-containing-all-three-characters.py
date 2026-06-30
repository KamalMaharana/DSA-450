class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the last seen index of 'a', 'b', and 'c'
        # Initialized to -1 because we haven't seen them yet
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            # Update the last seen position of the current character
            last_seen[char] = i
            
            # If all three characters have been seen at least once
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                # The smallest index among the three marks the end of the 
                # left-most valid boundary for a substring ending at index `i`.
                # Every index from 0 up to this minimum index can be a valid starting point.
                count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
                
        return count