# 문제: https://www.acmicpc.net/problem/11727 2xN 타일링 2
# 날짜: 2025-06-08
# 난이도: Silver III
# 문제유형: DP

# 문제 핵심
# 2xN 직사각형을 1x2, 2x1, 2x2 타일로 채우는 경우의 수를 구하라.
# 방법의 수를 10007로 나눈 나머지를 출력한다.

# 아이디어
#   점화식: dp[n] = dp[n - 1] + 2 * dp[n - 2]
# 이유
#   - dp[n - 1] 뒤에 2x1 타일을 세로로 붙이는 경우
#   - dp[n - 2] 뒤에 1x2 타일 2개 가로로, 또는 2x2 타일 1개 붙이는 경우 (2가지)

# 입력
# 정수 n (1 <= n <= 1000)

# 출력
# 타일링 경우의 수 % 10007

# 시간복잡도: O(N)
# 2번부터 n + 1까지 순회

# 공간복잡도: O(N)
# n + 1 크기 만큼의 배열

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def tile_case(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (dp[i - 2])) % 10007

    return dp[n]

n = int(input())

print(tile_case(n))