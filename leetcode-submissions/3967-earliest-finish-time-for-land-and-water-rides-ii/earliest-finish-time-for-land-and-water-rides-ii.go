func solve(startTime []int, duration []int, startTimeB []int, durationB []int) int {
    finish1 := 10000000
    for i := 0; i < len(startTime); i++ {
        finish1 = min(finish1, startTime[i] + duration[i])
    }

    finish2 := 10000000

    for i := 0; i < len(startTimeB); i++ {
        finish2 = min(finish2, max(startTimeB[i], finish1) + durationB[i])
    }
    return finish2
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
    landToWater := solve(landStartTime, landDuration, waterStartTime, waterDuration)
    waterToLand := solve(waterStartTime, waterDuration, landStartTime, landDuration)
    
    return min(landToWater, waterToLand)
}