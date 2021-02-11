// 1478. Allocate Mailboxes
// O(10^6)

package main

import (
	"math"
	"sort"
)

func minDistance(houses []int, k int) int {
	const inf = math.MaxInt32 / 2
	n := len(houses)
	// Adds two guard values.
	houses = append(houses, -inf, inf)
	sort.Ints(houses)

	// The min cost of interval [x, y] if we put mailboxes on house x and y.
	var between [105][105]int
	for x := 0; x < len(houses); x++ {
		for y := x + 1; y < len(houses); y++ {
			for m := x; m <= y; m++ {
				between[x][y] += min(houses[m]-houses[x], houses[y]-houses[m])
			}
		}
	}

	var solve func(int, int) int
	var memo [105][105]int
	for x := 0; x < n+2; x++ {
		for y := 0; y < n+2; y++ {
			memo[x][y] = -1
		}
	}
	solve = func(prev, cnt int) int {
		if cnt == k {
			return between[prev][n+1]
		}
		if memo[prev][cnt] != -1 {
			return memo[prev][cnt]
		}

		ans := inf
		for curr := prev + 1; curr <= n; curr++ {
			ans = min(ans, between[prev][curr]+solve(curr, cnt+1))
		}
		memo[prev][cnt] = ans
		return ans
	}
	return solve(0, 0)
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
