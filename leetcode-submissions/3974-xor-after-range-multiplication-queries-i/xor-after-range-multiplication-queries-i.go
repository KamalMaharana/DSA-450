func xorAfterQueries(nums []int, queries [][]int) int {
    // row := len(queries)
    // col := len(queries[0])
    for i := range queries {
        l := queries[i][0]
        r := queries[i][1]
        k := queries[i][2]
        v := queries[i][3]

        for l <= r {
            nums[l] = int((int64(nums[l]) * int64(v)) % 1000000007)
            l += k
        }
    }

    var result int
    for _, val := range nums {
        result = result ^ val
    }
    return result
}