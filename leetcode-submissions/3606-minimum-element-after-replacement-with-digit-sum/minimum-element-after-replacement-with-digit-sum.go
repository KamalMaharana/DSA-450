func sumOfDigits(num int) int {
    res := 0
    for num > 0 {
        res += num % 10
        num = int(num / 10)
    }
    return res
}
func minElement(nums []int) int {
    for i := 0; i < len(nums); i++ {
        nums[i] = sumOfDigits(nums[i])
    }
    return slices.Min(nums)
}