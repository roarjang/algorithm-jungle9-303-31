# 문제: https://www.acmicpc.net/problem/11053
# 날짜: 2025-06-11
# 난이도: SILVER II
# 문제유형: DP

# 문제 설명
# 수열 A에서 가장 긴 증가하는 부분 수열의 "길이"를 구하라"

# 핵심 아이디어 (DP 기반)
# 1. dp[i]:
#    arr[i]를 끝으로 하는 가장 긴 증가 부분 수열의 길이
# 2. prev[i]:
#    arr[i] 앞에 연결된 LIS 경로 상의 이전 원소의 인덱스 (LIS 경로 추적에 사용)
#    * prev는 수열 복원이 필요할 때만 사용됨

# 입력
# N: 수열 A의 크기 N (1 <= N <= 1000)
# A[0] ~ A[N-1]: 수열을 구성하는 정수들 (1 <= A[i] <= 1000)

# 출력
# 가장 긴 증가하는 부분 수열의 "길이"를 출력

# 시간복잡도
# O(N^2)
# 이유: 각 i에 대해 모든 j (j < i)를 순회하며 dp[i]를 갱신하기 때문

# 공간복잡도
# O(N)
# dp[] 배열과 (선택적으로) prev[] 배열에 N개의 값 저장


from sys import stdin
from typing import List

stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 최장 길이 찾기
def lis(arr: List[int]) -> int:
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)

# 최장 길이 찾기 + 수열 복원
# def lis(arr: List[int]) -> int:
#     n = len(A)
#     dp = [1] * n
#     prev = [-1] * n

#     for i in range(n):
#         for j in range(i):
#             if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
#                 dp[i] = dp[j] + 1
#                 prev[i] = j

#     # 최장 길이 및 끝 인덱스
#     lis_len = max(dp)
#     last_index = dp.index(lis_len)

#     # 수열 복원
#     lis = []
#     while last_index != -1:
#         lis.append(arr[last_index])
#         last_index = prev[last_index]

#     lis.reverse()

#     return lis # 수열 자체 반환

N = int(input())
A = list(map(int, input().split()))

print(lis(A))