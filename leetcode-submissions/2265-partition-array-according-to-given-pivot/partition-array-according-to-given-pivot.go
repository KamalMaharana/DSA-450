func pivotArray(nums []int, pivot int) []int {
    var less []int
    var equal []int
    var great []int
    var result []int

    for i := 0; i < len(nums); i++ {
        val := nums[i]
        if val < pivot {
            less = append(less, val)
        } else if val == pivot {
            equal = append(equal, val)
        } else {
            great = append(great, val)
        }
    }

    for i := range less {
        result = append(result, less[i])   
    }

    for i := range equal {
        result = append(result, equal[i])   
    }

    for i := range great {
        result = append(result, great[i])   
    }

    return result
}