func missingNumber(nums []int) int {
    n := len(nums)
    expected_sum := n*(n+1)/2
    actual_sum := 0

    for _, val:= range nums {
        actual_sum += val
    }
    return expected_sum - actual_sum
}