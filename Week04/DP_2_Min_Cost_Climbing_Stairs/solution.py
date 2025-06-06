# 문제: Min Cost Climbing Stairs (LeetCode 746)
# 날짜: 2025-06-07
# 난이도: 기초
# 문제유형: DP

# 문제 핵심
# 각 계단에는 비용이 있으며, 한 번에 한 계단 또는 두 계단을 올라갈 수 있다.
# 0번 또는 1번 인덱스에서 출발할 수 있으며, 도착 지점은 마지막 계단을 "넘는" 위치이다.
# 이때 도달 가능한 최소 비용을 구하는 문제이다.

# DP 알고리즘을 선택한 이유
# DP를 사용하면 부분 문제의 정답을 저장해 두었다가 재활용할 수 있으므로,
# 중복 계산을 피하고 효율적으로 정답을 구할 수 있다.

# 입력
# cost: 각 계단에 대응하는 비용이 담긴 정수 리스트

# 출력
# 정상(마지막 계단을 넘는 지점)까지 최소 비용으로 도달했을 때의 총 비용

# 시간복잡도
# O(N) - 계단 수만큼 순차적으로 연산

# 공간복잡도
# O(1) - 이전 두 결과만 기억하면 되므로 배열 사용 없이 최적화 가능

from sys import stdin
from typing import List
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def minCostClimbStairs(cost: List[int]) -> int:
    n = len(cost)

    if n == 0:
        return 0
    elif n == 1:
        return cost[0]
    
    # 초기값: 0번 또는 1번 계단에서 시작 가능 (비용 없음)
    prev2, prev1 = 0, 0

    for i in range(2, n + 1):
        one_step = prev1 + cost[i - 1]
        two_step = prev2 + cost[i - 2]
        curr = min(one_step, two_step)
        prev2, prev1 = prev1, curr

    return prev1

cost = list(map(int, input().split()))

print(minCostClimbStairs(cost))