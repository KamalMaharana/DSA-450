func getMinDistance(nums []int, target int, start int) int {
    var dist int
    dist = len(nums)
    for i, val := range nums {
        if val == target {
            temp := start - i
            res := len(nums)
            if temp < 0 {
                res = -temp
            } else {
                res = temp
            }
            dist = min(dist, res)
        }
    }
    return dist
}