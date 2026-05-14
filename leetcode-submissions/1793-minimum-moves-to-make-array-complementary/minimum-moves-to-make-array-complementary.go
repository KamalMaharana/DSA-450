func minMoves(nums []int, limit int) int {
    n := len(nums)
    // Difference array to track move counts for target sums from 2 to 2*limit
    diff := make([]int, 2*limit+2)

    for i := 0; i < n/2; i++ {
        a, b := nums[i], nums[n-1-i]
        
        // 1. Default: Assume 2 moves for all possible sums [2, 2*limit]
        diff[2] += 2
        diff[2*limit+1] -= 2
        
        // 2. Discount to 1 move: If sum is in [min(a,b)+1, max(a,b)+limit]
        minVal := min(a, b)
        maxVal := max(a, b)
        diff[minVal+1] -= 1
        diff[maxVal+limit+1] += 1
        
        // 3. Discount to 0 moves: If sum is exactly a + b
        diff[a+b] -= 1
        diff[a+b+1] += 1
    }

    // Sweep through the difference array to find the minimum moves
    ans := n // Maximum possible moves is n
    currentMoves := 0
    for i := 2; i <= 2*limit; i++ {
        currentMoves += diff[i]
        if currentMoves < ans {
            ans = currentMoves
        }
    }

    return ans
}

func min(a, b int) int {
    if a < b { return a }
    return b
}

func max(a, b int) int {
    if a > b { return a }
    return b
}