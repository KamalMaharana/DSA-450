func longestCommonPrefix(arr1 []int, arr2 []int) int {
    // 1. Create a set using a map with empty structs
    prefixes := make(map[int]struct{})
    
    // 2. Put all possible prefixes of each element in arr1 into the set
    for _, val := range arr1 {
        for val > 0 {
            prefixes[val] = struct{}{}
            val /= 10 // Chop off the last digit to get the next prefix
        }
    }
    
    maxLength := 0
    
    // 3. For each element in arr2, check its prefixes against our set
    for _, val := range arr2 {
        for val > 0 {
            // Check if the prefix exists in our "set"
            if _, exists := prefixes[val]; exists {
                // Calculate string length of the number
                length := len(strconv.Itoa(val))
                if length > maxLength {
                    maxLength = length
                }
                // Optimization: Once we find the longest valid prefix for this number,
                // smaller prefixes of the same number won't beat our current maxLength.
                break 
            }
            val /= 10
        }
    }
    
    return maxLength
}