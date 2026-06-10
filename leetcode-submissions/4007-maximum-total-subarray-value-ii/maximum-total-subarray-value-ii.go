package main

import (
	"container/heap"
	"math"
)

// Item stores the subarray state in the priority queue
type Item struct {
	value int
	l     int
	r     int
}

type MaxHeap []Item

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].value > h[j].value } // Max-heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(Item)) }
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[0 : n-1]
	return item
}

func maxTotalValue(nums []int, k int) int64 {
	n := len(nums)
	if n == 0 || k == 0 {
		return 0
	}

	// 1. Build Sparse Tables for O(1) Range Max and Min Queries
	maxLog := int(math.Log2(float64(n))) + 1
	stMax := make([][]int, n)
	stMin := make([][]int, n)
	for i := range stMax {
		stMax[i] = make([]int, maxLog)
		stMin[i] = make([]int, maxLog)
		stMax[i][0] = nums[i]
		stMin[i][0] = nums[i]
	}

	for j := 1; j < maxLog; j++ {
		for i := 0; i+(1<<j)<= n; i++ {
			stMax[i][j] = max(stMax[i][j-1], stMax[i+(1<<(j-1))][j-1])
			stMin[i][j] = min(stMin[i][j-1], stMin[i+(1<<(j-1))][j-1])
		}
	}

	// Helper function to query subarray value in O(1)
	queryValue := func(l, r int) int {
		length := r - l + 1
		j := int(math.Log2(float64(length)))
		mx := max(stMax[l][j], stMax[r-(1<<j)+1][j])
		mn := min(stMin[l][j], stMin[r-(1<<j)+1][j])
		return mx - mn
	}

	// 2. Initialize Priority Queue with (l, n-1) for all l
	h := &MaxHeap{}
	heap.Init(h)
	for l := 0; l < n; l++ {
		val := queryValue(l, n-1)
		heap.Push(h, Item{value: val, l: l, r: n - 1})
	}

	// 3. Extract top k values
	var totalValue int64 = 0
	for i := 0; i < k && h.Len() > 0; i++ {
		top := heap.Pop(h).(Item)
		totalValue += int64(top.value)

		// If there is a next valid subarray to the left, push it
		if top.r > top.l {
			nextR := top.r - 1
			nextVal := queryValue(top.l, nextR)
			heap.Push(h, Item{value: nextVal, l: top.l, r: nextR})
		}
	}

	return totalValue
}

func max(a, b int) int { if a > b { return a }; return b }
func min(a, b int) int { if a < b { return a }; return b }