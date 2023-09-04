class Solution:
    def minWindow(self, search_string: str, target: str) -> str:
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        required_len = len(target)        
        def found_target(required_len):
            return required_len == 0

        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
            curr = search_string[end]
            if target_letter_counts[curr] > 0:
                required_len -= 1

            # Decrease the letter count for the current letter
            # If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[curr] -= 1
            
            # If all letters in the target are found:
            while found_target(required_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    # Note the new minimum window,
                    # Take a slice of it
                    min_window = search_string[start : end + 1]
                
                # --------------------------------------------------
                # Here starts the window shrinking part
                # We will move start pointer ahead
                # This means we will need to remove/decrement the character at start

                # Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
                # As we know, all other characters not present in target
                # will become -ve in the map.
                # And all required chars will be 0 at this point
                # As we move start, if start is the required target chracter
                # Then removing it means window broken 
                # we would require that character again
                # If all target letters have been seen and now, 
                # a target letter is seen with count > 0
                # Increase the target length to be found.
                if target_letter_counts[search_string[start]] > 0:
                    required_len += 1
                    
                start+=1
                
        return min_window