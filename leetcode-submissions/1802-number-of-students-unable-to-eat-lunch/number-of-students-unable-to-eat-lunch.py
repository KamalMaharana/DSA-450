class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = Counter(students)
        n = len(students)
        k = 0
        while k < n and freq[sandwiches[k]]:
            freq[sandwiches[k]] -= 1
            k += 1
        return n - k