# 문제: https://www.acmicpc.net/problem/1463 Make it One
# 날짜: 2025-06-07
# 난이도: SILVER III
# 문제유형: DP

# 문제 핵심
# 정수 N을 1로 만들기 위한 최소 연산 횟수를 구한다.
# 사용할 수 있는 연산:
#   1. X가 3으로 나누어떨어지면 3으로 나눈다.
#   2. X가 2로 나누어떨어지면 2로 나눈다.
#   3. 1을 뺀다.

# 핵심 아이디어
# DP[i] = i를 1로 만드는 최소 연산 횟수
# 점화식
#   dp[i] = min(
#       dp[i - 1] + 1,
#       dp[i // 2] + 1 (if i % 2 == 0),
#       dp[i // 3] + 1 (if i % 3 == 0)
#   )

# 입력
# 정수 N이 주어진다. (1 <= N <= 106)

# 출력
# 최소 연산 횟수를 출력하기

# 시간복잡도: O(N)
# dp[2]부터 dp[N]까지 1회씩 순회

# 공간복잡도: O(N)
# dp 배열에 N + 1 크기 저장

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def min_operate_count(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

N = int(input())

print(min_operate_count(N))