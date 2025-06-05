# 문제: https://www.acmicpc.net/problem/11047
# 날짜: 2025-06-05
# 난이도: SILVER IV
# 문제유형: Greedy

# 문제 핵심
# 총 N종류의 동전을 사용하여 목표 금액 K를 만들 때,
# 필요한 동전 개수의 최소값을 구하는 문제

# 왜 이게 그리디인가?
# 동전의 가치가 큰 것부터 먼저 선택하면, 전체 개수를 최소화할 수 있기 때문
# -> 동전 가치가 배수 관계를 이루고 있어 그리디가 항상 최적해를 보장함
# (큰 동전이 항상 작은 동전 여러 개를 대체 가능)
# 만약, 동전이 배수 관계 아닐 때 -> 작은 동전 조합이 더 유리할 수도 있어서 오답 가능

# 입력
# 1. 동전 종류 N (1 <= N <= 10), 목표 금액 K (1 <= K <= 100,000,000)
# 2. 이후 N줄에 걸쳐 동전의 가치가 오름차순으로 주어짐

# 출력
# 목표 금액 K를 만들기 위해 사용한 동전의 최소 개수

# 시간복잡도
# 동전 종류 N개를 한 번씩 순회 -> O(N)
# 공간복잡도
# 동전 종류를 저장하는 리스트 사용 -> O(N)

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def minimum_coin(coin_values, target_money):
    coin_values.sort(reverse = True) # 큰 동전부터 사용
    count = 0

    for coin in coin_values:
        quotient = target_money // coin
        target_money -= (quotient * coin)
        count += quotient

    return count

# 입력
N, K = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

# 출력
print(minimum_coin(coin_values, target_money = K))