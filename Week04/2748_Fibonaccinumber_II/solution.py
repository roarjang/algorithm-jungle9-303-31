# 문제: https://www.acmicpc.net/problem/2748 / 피보나치 수 2
# 날짜: 2025-06-07
# 난이도: BRONZE I
# 문제유형: DP

# 문제 핵심
# 피보나치 수열의 n번째 값을 구하는 문제
# 피보나치 수열은 다음과 같이 정의된다.
#   - F(0) = 0
#   - F(1) = 1
#   - F(n) = F(n - 1) + F(n - 2) (n >= 2)

# DP 알고리즘을 선택한 이유
# 피나보나치 수열을 단순 재귀로 구현하면,
# 같은 값을 여러 번 계산하는 중복 연산이 발생한다.

# 예시: F(4)를 계산할 경우
#   F(4) = F(3) + F(2)
#        = (F(2) + F(1)) + (F(1) + F(0))
#        -> F(1)이 두 번 이상 호출됨

# 이러한 중복을 피하기 위해, 계산된 값을 저장(memoization) 하여
# 다시 계산하지 않고 재사용하는 방식이 필요하다.

# 따라서 피보나치 수를 효율적으로 구하기 위해
# 동적 계획법(Dynamic Programming, DP)을 사용하는 것이 적합하다.

# 입력
# 정수 n이 주어진다. (0 <= n <= 90)
# 이는 n번째 피보나치 수를 의미한다.

# 출력
# n번째 피보나치 수를 출력한다.

# 시간복잡도:
#   - Top-Down (memoization): O(n)
#   - Bottom-Up: O(n)
#   - Bottom-Up + 공간 최적화: O(n)

# 공간복잡도:
#   - Top-Down (memoization): O(n)
#   - Bottom-Up: O(n)
#   - Bottom-Up + 공간 최적화: O(1)

# 보너스팁
# 재귀의 공간 최적화가 불가능한 이유
#   - 스택 사용: 재귀는 호출될 때마다 스택 프레임을 차지한다. -> 누적됨
#   - 중간 값 저장: 재귀는 값 재사용이 어렵고, 이전 결과를 저장해도 호출 스택은 여전히 존재
#   - 공간 최적화 한계: 변수로 계산값만 들고 있으면 되는데, 재귀는 그걸 못 함

from sys import stdin
from typing import Dict
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 1. Top-Down (재귀 + 메모이제이션)
# 핵심: 중복 계산을 막기 위해 momization 사용
# 장점: 구현이 직관적이고 간단함
# 단점: 재귀 깊이가 깊어질 경우 스택 오버플로우 위험
def fib_recursive_memo(n: int, memo: Dict[int, int] = None) -> int:
    if memo is None:
        memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]
    
    memo[n] = fib_recursive_memo(n - 1, memo) + fib_recursive_memo(n - 2, memo)

    return memo[n]

# 2. Bottom-Up (반복문 + DP 테이블)
# 핵심: 작은 문제부터 차례로 해결하면서 결과를 배열(dp)에 저장
# 장점: 중복 계산 없음 -> 시간 효율 좋음 O(N)
# 단점: n + 1 크기의 배열 사용 -> 메모리 사용량이 상대적으로 큼 O(N) 공간
def fib_memo(n: int) -> int:
    if n == 0: return 0
    elif n == 1: return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 3. Bottom-Up + 공간 최적화
# 핵심: dp 배열 없이 두 변수(prev2, prev1) 만으로 계산
# 장점: 메모리 사용 최소화 O(1) 공간, 가장 효율적이고 빠르다.
# 단점: 중간 과정이 저장되지 않음 -> 모든 피보나치 수를 구할 수 없음
def fib_memo_space(n: int) -> int:
    if n == 0: return 0
    elif n == 1: return 1

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    
    return prev1

# 입력
n = int(input())

print(f"1. 재귀 + 메모이제이션: {fib_recursive_memo(n)}")
print(f"2. 반복문 + DP테이블: {fib_memo(n)}")
print(f"3. 반복문 + 공간 최적화: {fib_memo_space(n)}")