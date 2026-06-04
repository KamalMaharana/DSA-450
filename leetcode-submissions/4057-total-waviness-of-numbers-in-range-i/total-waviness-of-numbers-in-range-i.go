func totalWaviness(num1 int, num2 int) int {
    var res int
    for i := num1; i <= num2; i++ {
        val := fmt.Sprintf("%d", i)
        for j := 1; j < len(val) - 1; j++ {
            center := val[j]
            left := val[j - 1]
            right := val[j + 1]
            if (center > left && center > right) || (center < left && center < right) {
                res++
            }
        }
    }
    return res
}