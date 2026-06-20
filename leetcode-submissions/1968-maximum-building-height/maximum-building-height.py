class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Include the base restriction for building 1
        restrictions.append([1, 0])
        
        # 2. Sort by building ID to enable sequential linear scans
        restrictions.sort(key=lambda x: x[0])
        
        m = len(restrictions)
        
        # 3. Forward Pass: Propagate constraints from left to right
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # 4. Backward Pass: Propagate constraints from right to left
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # 5. Calculate global maximum height
        max_height = 0
        
        # Check intermediate peaks between restricted buildings
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            peak = (h1 + h2 + (id2 - id1)) // 2
            if peak > max_height:
                max_height = peak
                
        # Check the rightmost boundary case up to building n
        id_last, h_last = restrictions[-1]
        final_peak = h_last + (n - id_last)
        max_height = max(max_height, final_peak)
        
        return max_height