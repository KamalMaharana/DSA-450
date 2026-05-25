func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    if s[n-1] == '1' {
        return false
    }

    // dp[i] will store whether index i is reachable
    dp := make([]bool, n)
    dp[0] = true // We start at index 0

    // reachableCount keeps track of how many true positions 
    // are inside the current window [i - maxJump, i - minJump]
    reachableCount := 0

    for i := 1; i < n; i++ {
        // 1. Add the new element entering the window from the right
        if i >= minJump && dp[i-minJump] {
            reachableCount++
        }
        
        // 2. Remove the old element leaving the window from the left
        if i > maxJump && dp[i-maxJump-1] {
            reachableCount--
        }

        // 3. If s[i] is '0' and there is at least one reachable index 
        // within our jumping window, then index i is reachable.
        if s[i] == '0' && reachableCount > 0 {
            dp[i] = true
        }
    }

    return dp[n-1]
}