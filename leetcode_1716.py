class Solution:
    def totalMoney(self, n: int) -> int:
        if n == 0:
            return 0

        total = 0
        cycle = 1
        while n > 7:
            total += (cycle + 3) * 7
            n -= 7
            cycle += 1
        total += (cycle + cycle + n - 1) * n // 2
        return total
