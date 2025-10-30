# Difficulty - EASY

#  def distMoney(self, money: int, children: int) -> int:
#         if money < children:
#             return -1

#         if money > children * 8:
#             return children - 1

#         if money == (children * 8) - 4:
#             return children - 2

#         return (money - children) // 7

'''
Intuition:
The problem asks for the maximum number of children who can receive exactly 8 dollars, given an amount of money and a number of children. There are a few constraints:
1. Every child must receive at least 1 dollar.
2. The total money distributed must be equal to the given `money`.

First, let's handle the base cases:
- If `money < children`, it's impossible to give each child at least 1 dollar, so we return -1.

Now, let's give each of the `children` 1 dollar. This is the minimum requirement. The remaining money is `money - children`.
Let's call this remaining money `remaining_money`.
Each of the children who will receive 8 dollars, needs an additional 7 dollars (since they already have 1).
So, the number of children who can receive 8 dollars is `remaining_money // 7`.

Let's call the number of children who can receive 8 dollars `k`.
`k = (money - children) // 7`.

Now, we need to consider the edge cases:
- What if all children get 8 dollars? This happens when `money = children * 8`. In this case, `k = (8 * children - children) // 7 = 7 * children // 7 = children`. So, all `children` get 8 dollars.
- What if `money > children * 8`? This means after giving every child 8 dollars, we still have some money left over. The problem states that the total money distributed must be equal to the given `money`. So, we can't just give everyone 8 dollars. We have to distribute the remaining money to one of the children. This means one child will have more than 8 dollars, and the rest `children - 1` will have 8 dollars. So, the answer is `children - 1`.
- What if we have `k` children with 8 dollars, and the last child has 4 dollars?
  - Let's say we have `children - 1` children with 8 dollars. The total money distributed is `(children - 1) * 8`.
  - The remaining money is `money - (children - 1) * 8`. This money goes to the last child.
  - If this remaining money is 4, we have a problem. The last child has 4 dollars. We can't have this.
  - So, we must take 1 dollar from one of the children who has 8 dollars and give it to the child who has 4 dollars.
  - This means one child will have 7 dollars, one will have 5 dollars, and `children - 2` will have 8 dollars.
  - So, the number of children with 8 dollars is `children - 2`.
  - This happens when `money - (children - 1) * 8 = 4`, which simplifies to `money = 8 * children - 8 + 4 = 8 * children - 4`.
  - So, if `money == children * 8 - 4`, the answer is `children - 2`.

- In all other cases, the number of children who can get 8 dollars is `k = (money - children) // 7`.

Let's summarize the logic:
1. If `money < children`, return -1.
2. Give 1 dollar to each child. `money_left = money - children`.
3. The number of children who can get an additional 7 dollars is `money_left // 7`. Let this be `ans`.
4. If `ans == children` and `money_left % 7 == 0`, it means all children get 8 dollars. Return `children`.
5. If `ans == children` and `money_left % 7 != 0`, it means `children-1` children get 8 dollars and the last one gets `1 + 7 + money_left % 7` which is more than 8. So return `children-1`.
   This is equivalent to `money > children * 8`.
6. If `ans == children - 1` and `money_left % 7 == 3` (which means the last child has `1+3=4` dollars), we have to take 1 dollar from a child with 8 dollars and give it to the one with 4. So we have `children-2` children with 8 dollars.
   This is equivalent to `money == children * 8 - 4`.
7. Otherwise, the answer is `ans`.

Example Walkthrough:
`money = 20`, `children = 3`
1. `money > children`.
2. Give each child 1 dollar. `remaining_money = 20 - 3 = 17`.
3. `k = 17 // 7 = 2`.
4. We have 2 children with 8 dollars. The remaining money is `17 % 7 = 3`.
5. The third child gets `1 + 3 = 4` dollars.
6. This is the case where one child has 4 dollars. But wait, `k` is not `children - 1`. `k` is 2, `children - 1` is 2. So `k == children - 1`.
   `money_left % 7 = 3`. So this is the edge case.
   `20 == 3 * 8 - 4` => `20 == 20`. Yes.
   So, the answer is `children - 2 = 3 - 2 = 1`.
   Let's verify. We have 1 child with 8 dollars. Remaining money is `20 - 8 = 12`. We have 2 children left. We can give them 6 and 6. So, `(8, 6, 6)`. This is a valid distribution. Number of children with 8 dollars is 1.

Let's try another example. `money = 16`, `children = 2`.
1. `money > children`.
2. `remaining_money = 16 - 2 = 14`.
3. `k = 14 // 7 = 2`.
4. `k == children`. `14 % 7 == 0`. So, all children get 8 dollars. Answer is 2.
   Distribution: `(8, 8)`.

Let's try another example. `money = 2`, `children = 2`.
1. `money == children`.
2. `remaining_money = 2 - 2 = 0`.
3. `k = 0 // 7 = 0`.
4. The answer is 0.
   Distribution: `(1, 1)`.

Let's try another example. `money = 13`, `children = 3`.
1. `money > children`.
2. `remaining_money = 13 - 3 = 10`.
3. `k = 10 // 7 = 1`.
4. `k` is not `children` or `children - 1`. So the answer is `k = 1`.
   Distribution: one child gets 8. `13 - 8 = 5` for the other two. We can give them 2 and 3. So `(8, 2, 3)`. Valid.

Final simplified logic:
1. If `money < children`, return -1.
2. If `money > children * 8`, return `children - 1`.
3. If `money == children * 8 - 4`, return `children - 2`.
4. Otherwise, return `(money - children) // 7`.

Time Complexity:
O(1), as we are doing a few calculations.

Space Complexity:
O(1), as we are not using any extra space.
'''