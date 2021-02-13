// 10. Regular Expression Matching

type token struct {
	c    byte
	star bool
}

func isMatch(s string, p string) bool {
	tokens := make([]token, 0)
	for x := 0; x < len(p); {
		if x+1 < len(p) && p[x+1] == '*' {
			tokens = append(tokens, token{p[x], true})
			x += 2
		} else {
			tokens = append(tokens, token{p[x], false})
			x++
		}
	}

	s = "#" + s
	tokens = append([]token{{'#', false}}, tokens...)

	canMatch := func(x, y int) bool {
		return s[x] == tokens[y].c || tokens[y].c == '.'
	}

	var dp [25][35]bool
	dp[0][0] = true
	for y := 1; y < len(tokens) && tokens[y].star; y++ {
		dp[0][y] = true
	}
	for x := 1; x < len(s); x++ {
		for y := 1; y < len(tokens); y++ {
			if tokens[y].star {
				// Ignores tokens[y].
				dp[x][y] = dp[x][y] || dp[x][y-1]
				// Matches s[x] with tokens[y].
				dp[x][y] = dp[x][y] || (canMatch(x, y) && dp[x-1][y])
			} else {
				// Matches s[x] with tokens[y].
				dp[x][y] = dp[x][y] || (canMatch(x, y) && dp[x-1][y-1])
			}
		}
	}
	return dp[len(s)-1][len(tokens)-1]
}
