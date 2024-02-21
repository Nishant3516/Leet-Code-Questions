class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            horizontal_time = abs(x2 - x1)
            vertical_time = abs(y2 - y1)
            diagonal_time = max(horizontal_time, vertical_time)

            total_time += diagonal_time

        return total_time
