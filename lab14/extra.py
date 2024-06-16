import time
import numpy as np

def dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def cost_of_triangle(p1, p2, p3):
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)

#Rekurencja
def min_cost_triangulation_recursive(points, i, j):
    if j <= i + 1:
        return 0

    min_cost = float('inf')
    for k in range(i+1, j):
        cost = (min_cost_triangulation_recursive(points, i, k) +
                min_cost_triangulation_recursive(points, k, j) +
                cost_of_triangle(points[i], points[k], points[j]))
        if cost < min_cost:
            min_cost = cost

    return min_cost

#DP
def min_cost_triangulation_dp(points):
    n = len(points)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + cost_of_triangle(points[i], points[k], points[j])
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][-1]

if __name__ == '__main__':
    points1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    points2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    start_time = time.time()
    recursive_cost1 = min_cost_triangulation_recursive(points1, 0, len(points1) - 1)
    recursive_time1 = time.time() - start_time

    start_time = time.time()
    recursive_cost2 = min_cost_triangulation_recursive(points2, 0, len(points2) - 1)
    recursive_time2 = time.time() - start_time

    start_time = time.time()
    dp_cost1 = min_cost_triangulation_dp(points1)
    dp_time1 = time.time() - start_time

    start_time = time.time()
    dp_cost2 = min_cost_triangulation_dp(points2)
    dp_time2 = time.time() - start_time

    print(f"Koszt rekurencyjny dla points1: {recursive_cost1}, time: {recursive_time1:.6f} s")
    print(f"Koszt DP dla points1: {dp_cost1}, time: {dp_time1:.6f} s")
    print(f"Koszt rekurencyjny dla points2: {recursive_cost2}, time: {recursive_time2:.6f} s")
    print(f"Koszt DP for points2: {dp_cost2}, time: {dp_time2:.6f} s")
