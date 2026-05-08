package main

const MAX = 1000001

// Global variables for precomputation
var spf [MAX]int
var initialized bool

func initSieve() {
	if initialized {
		return
	}
	for i := 2; i < MAX; i++ {
		spf[i] = i
	}
	for i := 2; i*i < MAX; i++ {
		if spf[i] == i {
			for j := i * i; j < MAX; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}
	initialized = true
}

func minJumps(nums []int) int {
	initSieve()
	n := len(nums)
	if n <= 1 {
		return 0
	}

	// bucket[p] maps prime p to all indices j where nums[j] % p == 0
	bucket := make(map[int][]int)
	for i, val := range nums {
		temp := val
		for temp > 1 {
			p := spf[temp]
			bucket[p] = append(bucket[p], i)
			for temp%p == 0 {
				temp /= p
			}
		}
	}

	// BFS setup
	queue := []int{0}
	visitedIdx := make([]bool, n)
	visitedPrimes := make(map[int]bool)
	visitedIdx[0] = true
	steps := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			curr := queue[0]
			queue = queue[1:]

			if curr == n-1 {
				return steps
			}

			// 1. Adjacent Steps (i+1, i-1)
			neighbors := []int{curr - 1, curr + 1}
			for _, next := range neighbors {
				if next >= 0 && next < n && !visitedIdx[next] {
					visitedIdx[next] = true
					queue = append(queue, next)
				}
			}

			// 2. Prime Teleportation
			// If nums[curr] is prime, we can jump to any index divisible by that prime
			if isPrime(nums[curr]) {
				p := nums[curr]
				if !visitedPrimes[p] {
					for _, next := range bucket[p] {
						if !visitedIdx[next] {
							visitedIdx[next] = true
							queue = append(queue, next)
						}
					}
					// CRITICAL: Clear the bucket to avoid O(N^2) behavior
					delete(bucket, p)
					visitedPrimes[p] = true
				}
			}
		}
		steps++
	}

	return -1
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	return spf[n] == n
}