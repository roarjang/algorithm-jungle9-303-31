# 문제: https://www.acmicpc.net/problem/9084 Coin
# 날짜: 2025-06-10
# 난이도: GOLD V
# 문제유형: DP

# 문제 핵심
# 동전은 무한히 사용할 수 있다.
# 서로 다른 동전들을 조합해서 목표 금액을 만드는 경우의 수를 구한다.
# 조합의 순서는 중요하지 않다. 

# 알고리즘 설명
# dp[i]: i원을 만들 수 있는 조합의 수
# 초기값 dp[0] = 1 (0원을 만드는 경우는 아무 동전도 사용하지 않는 1가지)
# 각 동전에 대해 dp[coin]부터 dp[target]까지 누적 계산한다.
# dp[i] += dp[i - coin]: 이전 상태에서 coin 하나 추가해서 만드는 방식

# 입력
# 테스트 케이스 개수 T (1 <= T <= 10)
# 동전의 가지수 N (1 <= N <= 10)
# 목표 금액 M (1 <= M <= 10000)

# 출력
# N가지 동전으로 목표 금액을 만드는 모든 방법의 수를 출력한다.

# 시간복잡도: O(N * M)
# N: 동전의 종류 수
# M: 목표 금액
# 각 동전에 대해 목표 금액까지 순회

# 공간복잡도: O(M)
# 목표 금액만큼 1차원 dp 배열 사용

from sys import stdin
from typing import List

# 입력 파일에서 읽기
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def case_coin(N: int, coins: List[int], target: int) -> int:
    """
    dp[i]: i원을 만들 수 있는 경우의 수
    동전의 조합(순서 무시)을 구하기 때문에
    작은 동전부터 누적하며 계산한다.
    """
    dp = [0] * (target + 1)
    dp[0] = 1 # 0d원을 만드는 경우는 '아무것도 사용하지 않음' 1가지

    for coin_value in coins:
        for amount in range(coin_value, target + 1):
            dp[amount] += dp[amount - coin_value]

    return dp[target]

# 테스트 케이스 수
T = int(input())

for i in range(T):
    N = int(input()) # 동전 종류 수
    coins = list(map(int, input().split())) # 동전 리스트
    target = int(input()) # 목표 금액

    print(case_coin(N, coins, target))