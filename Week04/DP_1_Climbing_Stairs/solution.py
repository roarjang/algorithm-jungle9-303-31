# 문제: DP_1_Climbing_Stairs (LeetCode 70)
# 날짜: 2025-06-06
# 난이도: 기초
# 문제유형: DP

# 문제 핵심
# 계단 n개를 한 번에 1칸 또는 2칸씩 오를 수 있다.
# 정상(n번째 계단)까지 도달하는 서로 다른 방법의 수를 구하는 문제
# 피보나치 수열 형태의 점화식을 가진다.

# DP 알고리즘을 선택한 이유
# DP를 사용하면 부분 문제의 정답을 저장해 두었다가 재활용할 수 있으므로,
# 중복 계산을 피하고 효율적으로 정답을 구할 수 있다.

# 입력
# n: 계단의 총 개수 (정수)

# 출력
# n번째 계단(정상)까지 오를 수 있는 서로 다른 방법의 수

# 시간복잡도
# O(N) - 계단 2부터 n까지 한 번씩만 계산함

# 공간복잡도
# O(N) - dp 배열을 n + 1 크기로 사용하여 메모이제이션 수행
# (단, 이전 두 값만 사용하므로 공간을 O(1)로 최적화 가능)

# 공간 복잡도 최적화
# dp[i]는 오직 dp[i-1], dp[i-2]만 참조하므로
# 전체 배열을 유지할 필요 없이 이전 두 값만 저장하면 O(1)로 최적화할 수 있다.

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def climbStairs(n: int) -> int:
    # Base cases: 0 or 1 step
    if n <= 1:
        return 1
    
    prev2, prev1 = 1, 1 # dp[0], dp[1]
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1

n = int(input())

print(climbStairs(n))

# 메모이제이션 활용

# from sys import stdin
# stdin = open('input.txt', 'r')
# input = lambda: stdin.readline().strip()

# def climbStairs(n: int) -> int:
#     # Base cases: 0 or 1 step
#     if n <= 1:
#         return 1
    
#     # dp[i]는 i번째 계단에 도달하는 방법의 수
#     dp = [0] * (n + 1)
#     dp[0] = 1 # 0번째 계단까지 도달하는 방법 1가지
#     dp[1] = 1 # 1번째 계단까지 도달하는 방법 1가지

#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]

# n = int(input())

# print(climbStairs(n))