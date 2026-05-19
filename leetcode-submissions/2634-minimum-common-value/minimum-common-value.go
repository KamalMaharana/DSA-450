func getCommon(nums1 []int, nums2 []int) int {
    i := 0
    j := 0

    // Traverse both arrays using two pointers
    for i < len(nums1) && j < len(nums2) {
        if nums1[i] == nums2[j] {
            return nums1[i] // Found the smallest common element
        } else if nums1[i] > nums2[j] {
            j++ // Move the second pointer if its value is smaller
        } else {
            i++ // Move the first pointer if its value is smaller
        }
    }

    // If we break out of the loop, no common element exists
    return -1
}