# 문제: https://www.acmicpc.net/problem/11053
# 날짜: 2025-06-11
# 난이도: SILVER II
# 문제유형: DP

# 문제 핵심


# _ 알고리즘을 적용한 이유


# 입력


# 출력


# 시간복잡도


# 공간복잡도


from sys import stdin
from typing import List

stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def lis(A: List[int], N: int) -> int:
    n = N
    seq = A

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = 1
        for j in range(1, n + 1):
            if seq[j - 1] < seq[i - 1]:
                dp[j] = dp[j - 1] + 1

    return dp[6]

N = int(input())
A = list(map(int, input().split()))

print(list(A), N)

print(lis(A, N))