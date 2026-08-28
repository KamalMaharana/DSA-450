# lexPalindromicPermutation
from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        from collections import Counter
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]

        # Feasibility: palindrome permutation must exist
        if (n % 2 == 0 and odd_chars) or (n % 2 == 1 and len(odd_chars) != 1):
            return ""

        half = {c: cnt[c] // 2 for c in cnt}
        mid = odd_chars[0] if n % 2 == 1 else None
        half_len = n // 2

        def build_from(prefix_counts, prefix_chars):
            # fill remaining half positions ascending, using up prefix_counts
            rest = []
            for c in sorted(prefix_counts):
                rest.extend([c] * prefix_counts[c])
            H = prefix_chars + rest
            if mid is not None:
                return "".join(H) + mid + "".join(reversed(H))
            return "".join(H) + "".join(reversed(H))

        best = None
        remaining = dict(half)
        prefix_chars = []

        for i in range(half_len):
            # try to place a letter > target[i] using 'remaining'
            for c in sorted(remaining):
                if remaining[c] > 0 and c > target[i]:
                    trial = dict(remaining)
                    trial[c] -= 1
                    cand = build_from(trial, prefix_chars + [c])
                    if cand > target and (best is None or cand < best):
                        best = cand
                    break
            # now try to extend exact match with target[i]
            c = target[i]
            if remaining.get(c, 0) > 0:
                remaining[c] -= 1
                prefix_chars.append(c)
            else:
                break  # can't extend prefix match further
        else:
            # first half can exactly equal target's first half
            if mid is not None:
                if mid > target[half_len]:
                    cand = build_from(remaining, prefix_chars)  # remaining is now empty
                    if cand > target and (best is None or cand < best):
                        best = cand
                elif mid == target[half_len]:
                    cand = build_from(remaining, prefix_chars)
                    if cand > target and (best is None or cand < best):
                        best = cand
            else:
                cand = build_from(remaining, prefix_chars)
                if cand > target and (best is None or cand < best):
                    best = cand

        return best if best is not None else ""