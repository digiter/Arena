// 1458. Max Dot Product of Two Subsequences
// O(500^2), 356 ms
import "math/big"

func maxDotProduct(nums1 []int, nums2 []int) int {
	var solve func(int, int) *big.Int
	var memo [505][505]*big.Int
	solve = func(x, y int) *big.Int {
		if x == -1 || y == -1 {
			return big.NewInt(0)
		}
		if memo[x][y] != nil {
			return memo[x][y]
		}

		// ans = solve(x-1, y-1)
		// ans = max(ans, solve(x-1, y-1) + nums1[x] * nums1[y])
		ans := clone(solve(x-1, y-1))
		if nums1[x]*nums2[y] > 0 {
			ans.Add(ans, big.NewInt(int64(nums1[x]*nums2[y])))
		}
		ans = max(ans, solve(x-1, y))
		ans = max(ans, solve(x, y-1))
		memo[x][y] = clone(ans)
		return ans
	}

	ans := big.NewInt(int64(nums1[0] * nums2[0]))
	for x, _ := range nums1 {
		for y, _ := range nums2 {
			// ans = max(ans, nums1[x] * nums2[y] + solve(x-1, y-1))
			t := clone(solve(x-1, y-1))
			t.Add(t, big.NewInt(int64(nums1[x]*nums2[y])))
			ans = max(ans, t)
		}
	}
	return int(ans.Int64())
}

func clone(x *big.Int) *big.Int {
	return new(big.Int).Set(x)
}

func max(x, y *big.Int) *big.Int {
	if x.Cmp(y) == +1 {
		return x
	}
	return y
}
