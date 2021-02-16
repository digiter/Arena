// 97. Interleaving String
// O(100 * 100)
func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1) == 0 {
		return s2 == s3
	}
	if len(s2) == 0 {
		return s1 == s3
	}
	if len(s1)+len(s2) != len(s3) {
		return false
	}

	var dp [105][105]bool
	sub := func(x, y int) bool {
		if x == -1 && y == -1 {
			return true
		}
		if x == -1 {
			return s2[:y+1] == s3[:y+1]
		}
		if y == -1 {
			return s1[:x+1] == s3[:x+1]
		}
		return dp[x][y]
	}
	for x, _ := range s1 {
		for y, _ := range s2 {
			z := (x + 1) + (y + 1) - 1
			if s1[x] == s3[z] {
				dp[x][y] = dp[x][y] || sub(x-1, y)
			}
			if s2[y] == s3[z] {
				dp[x][y] = dp[x][y] || sub(x, y-1)
			}
		}
	}
	return dp[len(s1)-1][len(s2)-1]
}
