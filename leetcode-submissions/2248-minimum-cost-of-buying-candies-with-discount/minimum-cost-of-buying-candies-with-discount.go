func minimumCost(cost []int) int {
    if len(cost) < 2 {
        return cost[0]
    }
    slices.Sort(cost)
    // fmt.Println(cost)
    i := len(cost) - 1
    var res int
    for i >= 1 {
        a := cost[i]
        b := cost[i - 1]
        res += (a + b)
        i = i - 3
    }

    if i >= 0 {
        res += cost[i]
    }
    return res
}