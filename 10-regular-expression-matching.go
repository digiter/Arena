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

	canMatch := func(x, y int) bool {
		return s[x] == tokens[y].c || tokens[y].c == '.'
	}

	var solve func(int, int) bool
	var memo, saved [25][35]bool
	solve = func(x, y int) bool {
		if x == len(s) {
			if y == len(tokens) {
				return true
			} else if tokens[y].star && solve(x, y+1) {
				return true
			} else {
				return false
			}
		}
		if y == len(tokens) {
			return false
		}

		if !tokens[y].star && canMatch(x, y) {
			memo[x][y] = solve(x+1, y+1)
			saved[x][y] = true
			return solve(x+1, y+1)
		} else if tokens[y].star {
			if solve(x, y+1) {
				return true
			}
			for x < len(s) && canMatch(x, y) {
				if solve(x+1, y+1) {
					memo[x][y] = true
					saved[x][y] = true
					return true
				}
				x++
			}
		}
		memo[x][y] = false
		saved[x][y] = false
		return false
	}
	return solve(0, 0)
}
