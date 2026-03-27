class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        # Reduce k to be within the bounds of the row length
        shift = k % n
        
        # If no effective shift is needed, it's immediately true
        if shift == 0:
            return True
            
        for row in mat:
            for j in range(n):
                # Check if the element matches the element 'shift' positions away
                # This covers both left and right shifts due to cyclic property
                if row[j] != row[(j + shift) % n]:
                    return False
                    
        return True