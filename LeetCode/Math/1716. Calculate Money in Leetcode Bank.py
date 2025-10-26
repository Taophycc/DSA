# Difficulty - EASY

#  def totalMoney(self, n: int) -> int:
#         mon = 1
#         day = 0
#         bank = 0

#         for i in range(n):
#             bank = bank + mon + day
#             day += 1

#             if day % 7 == 0:
#                 mon += 1
#                 day = 0

#         return bank

"""
### Explanation:

The problem asks us to calculate the total money saved in a bank over `n` days, following a specific pattern.

1.  **Understanding the Pattern:**
    *   **Week 1:** Starts with $1 on Monday, then $2 on Tuesday, ..., $7 on Sunday. The total for the first week is `1 + 2 + 3 + 4 + 5 + 6 + 7 = 28`.
    *   **Week 2:** Starts with $2 on Monday (which is $1 more than the previous Monday's deposit), then $3 on Tuesday, ..., $8 on Sunday. The total for the second week is `2 + 3 + 4 + 5 + 6 + 7 + 8 = 35`.
    *   **Week 3:** Starts with $3 on Monday, and so on. The total for the third week is `3 + 4 + 5 + 6 + 7 + 8 + 9 = 42`.

    We can observe that each subsequent full week adds $7 more than the previous full week. Specifically, for the `w`-th week (0-indexed, so `w=0` for the first week), the sum is `28 + 7 * w`.

2.  **Breaking Down `n` Days:**
    We can divide the total `n` days into two parts:
    *   `num_weeks`: The number of complete 7-day weeks. This is calculated as `n // 7`.
    *   `remaining_days`: The number of days left after the full weeks. This is calculated as `n % 7`.

3.  **Calculating Money from Full Weeks:**
    We iterate `num_weeks` times. In each iteration `w` (from `0` to `num_weeks - 1`), we add the sum for that week to `total_money`. The sum for week `w` is `28 + (7 * w)`.

4.  **Calculating Money from Remaining Days:**
    For the `remaining_days`, we need to determine the starting deposit for this partial week. Since `num_weeks` full weeks have passed, the next Monday's deposit (which would be the first day of this partial week if it were a Monday) would be `num_weeks + 1`.
    We then iterate `d` from `0` to `remaining_days - 1`. For each day, we add `(start_deposit_for_partial_week + d)` to `total_money`.

5.  **Example (n=10):**
    *   `num_weeks = 10 // 7 = 1`
    *   `remaining_days = 10 % 7 = 3`
    *   **Full Weeks:** For `w = 0` (the first week): `total_money += 28 + (7 * 0) = 28`.
    *   **Remaining Days:**
        *   `start_deposit_for_partial_week = 1 + 1 = 2`.
        *   For `d = 0`: `total_money += 2 + 0 = 2`. (Total = 28 + 2 = 30)
        *   For `d = 1`: `total_money += 2 + 1 = 3`. (Total = 30 + 3 = 33)
        *   For `d = 2`: `total_money += 2 + 2 = 4`. (Total = 33 + 4 = 37)
    *   Final `total_money = 37`.

This approach efficiently calculates the total money by leveraging the observed arithmetic progression in weekly sums and daily deposits.

### Complexity

*   **Time Complexity:** O(n) because we iterate through the number of weeks and remaining days, which is proportional to n.
*   **Space Complexity:** O(1) because we are not using any extra space that scales with the input size.
"""