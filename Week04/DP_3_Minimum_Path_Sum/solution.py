# 문제: Minimum Path Sum (LeetCode 64)
# 날짜: 2025-06-07
# 난이도: 기초
# 문제유형: DP

# 문제 핵심
# (m x n) 크기의 2차원 행렬 grid가 주어진다.
# 시작 지점은 (0, 0)이고, 종료 지점은 (m - 1, n - 1)이다.
# 오른쪽 또는 아래쪽으로만 이동 가능하다.
# 각 칸에는 이동 시 비용이 있으며, 총 비용이 최소가 되도록 이동해야 한다.

# DP 알고리즘을 선택한 이유
# DP를 사용하면 부분 문제의 정답을 저장해 두었다가 재활용할 수 있으므로,
# 중복 계산을 피하고 효율적으로 정답을 구할 수 있다.

# 입력
# grid: 각 칸에 대응하는 비용이 담긴 2차원 정수 리스트

# 출력
# 종료 지점까지 최소 비용으로 도달했을 때의 총 비용

# 시간복잡도: O(m * n) - 모든 칸을 한 번씩만 계산

# 공간복잡도: O(n) - 한 행(row)씩만 저장하여 공간 절약
from sys import stdin
from typing import List
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [0] * n

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[j] = grid[i][j] # 시작점
            elif i == 0:
                dp[j] = dp[j - 1] + grid[i][j] # 첫 행
            elif j == 0:
                dp[j] = dp[j] + grid[i][j] # 첫 열
            else:
                dp[j] = grid[i][j] + min(dp[j - 1], dp[j])  # 최소 누적 경로 선택

    return dp[n - 1]

grid = [list(map(int, input().split())) for _ in range(4)]

print(minPathSum(grid))

# 공간 복잡도 O(m x n)
# from sys import stdin
# from typing import List
# stdin = open('input.txt', 'r')
# input = lambda: stdin.readline().strip()

# def minPathSum(grid: List[List[int]]) -> int:
#     m, n = len(grid), len(grid[0])
#     dp = [[0] * n for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 dp[i][j] = grid[i][j] # 시작점
#             elif i == 0:
#                 dp[i][j] = dp[i][j - 1] + grid[i][j] # 첫 행
#             elif j == 0:
#                 dp[i][j] = dp[i - 1][j] + grid[i][j] # 첫 열
#             else:
#                 dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

#     return dp[m - 1][n - 1]


# grid = [list(map(int, input().split())) for _ in range(4)]

# print(minPathSum(grid))