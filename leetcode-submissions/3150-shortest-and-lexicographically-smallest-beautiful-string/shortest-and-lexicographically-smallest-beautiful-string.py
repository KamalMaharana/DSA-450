class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        ones = 0
        res = ""

        for j in range(n):
            if s[j] == "1":
                ones += 1

            # Shrink window if we have too many ones
            while ones > k:
                if s[i] == "1":
                    ones -= 1
                i += 1

            # Trim leading zeros to make the window as short as possible
            while i <= j and s[i] == "0" and ones == k:
                i += 1

            # Update result on exact match
            if ones == k:
                curr = s[i : j + 1]
                if not res or len(curr) < len(res) or (len(curr) == len(res) and curr < res):
                    res = curr

        return res