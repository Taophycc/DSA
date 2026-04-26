import "math"
func furthestDistanceFromOrigin(moves string) int {
    undefined_mov := 0
    res := 0

    for _, move := range moves {
        if move == 'L' {
            res += 1
        } else if move == 'R' {
            res -= 1
        } else {
            undefined_mov += 1
        }

    } 

    left_case := math.Abs(float64(res - undefined_mov))
    right_case := math.Abs(float64(res + undefined_mov))

    return int(math.Max(left_case, right_case))
}