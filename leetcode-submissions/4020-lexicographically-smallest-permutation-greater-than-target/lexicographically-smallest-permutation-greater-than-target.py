from collections import Counter


class Solution:

  def lexGreaterPermutation(self, s: str, target: str) -> str:
    n = len(s)
    total_counts = Counter(s)

    # 1. Determine how far we can match target exactly
    prefix_counts = [Counter()]
    matched_len = 0
    cur_counts = Counter()

    for ch in target:
      if cur_counts[ch] < total_counts[ch]:
        cur_counts[ch] += 1
        prefix_counts.append(cur_counts.copy())
        matched_len += 1
      else:
        break

    # 2. Iterate backwards from matched_len down to 0 to find divergence point
    for i in range(matched_len, -1, -1):
      # Available characters if we match target[0...i-1]
      used = prefix_counts[i]
      avail = total_counts - used

      if i < n:
        # Find the smallest character strictly greater than target[i]
        for ch_code in range(ord(target[i]) + 1, ord("z") + 1):
          ch = chr(ch_code)
          if avail[ch] > 0:
            avail[ch] -= 1
            # Construct suffix from remaining characters sorted
            suffix = "".join(sorted(avail.elements()))
            return target[:i] + ch + suffix

    return ""