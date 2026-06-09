func maxTotalValue(nums []int, k int) int64 {
    var min int
    var max int
    min = slices.Min(nums)
    max = slices.Max(nums)
    res := (max - min) * k
    return int64(res)
}