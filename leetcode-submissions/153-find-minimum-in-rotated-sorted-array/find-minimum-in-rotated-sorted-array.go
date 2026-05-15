func findMin(nums []int) int {
    low := 0
    high := len(nums) - 1

    for low < high {
        mid := low + (high-low)/2

        // If mid element is greater than the high element, 
        // the minimum must be in the right half.
        if nums[mid] > nums[high] {
            low = mid + 1
        } else {
            // Otherwise, the minimum is in the left half (including mid).
            high = mid
        }
    }

    return nums[low]
}