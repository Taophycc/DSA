class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        seen = set(friends)
        fn = []

        for i, c in enumerate(order):
            if c in seen:
                fn.append(c)
        return fn
