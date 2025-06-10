# 문제: https://www.acmicpc.net/problem/9251
# 날짜: 2025-06-10
# 난이도: GOLD V
# 문제유형: DP

# 문제 핵심
# LCS 문제는 두 수열이 주어졌을 때,
# 두 수열 모두에 공통으로 나타나는 부분 수열 중 가장 긴 것을 찾는 문제이다.

# 알고리즘 핵심
# 두 문자열 X와 Y의 각 문자를 비교하여 dp 테이블을 채운다.
#   {X1, X2, ... , Xm}, {Y1, Y2, ... , Yn}
# 1. 문자가 같으면 대각선 값에 1 더하기
#   if Xm == Yn: dp[i][j] = dp[i - 1][j - 1] + 1
# 2. 다르면 위나 왼쪽 중 큰 값 선택
#   if Xm != Yn: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 각각 주어진다.
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자이다.

# 출력
# 두 문자열의 LCS 길이를 출력하라.

# 시간복잡도: O(M * N), M과 N은 각각 두 문자열의 길이

# 공간복잡도: O(M * N)

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

def lcs_length(X: str, Y: str) -> int:
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def lcs_string(X: str, Y: str) -> str:
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    track = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                track[i][j] = 1 # 대각선
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    track[i][j] = 2 # 위쪽
                else:
                    dp[i][j] = dp[i][j - 1]
                    track[i][j] = 3 # 왼쪽

    # 역추적하여 LCS 문자열 복원
    i, j = m, n
    lcs_chars = []

    while i > 0 and j > 0:
        if track[i][j] == 1: # 대각선: 문자가 같음
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        elif track[i][j] == 2: # 위쪽 이동
            i -= 1
        else: # 왼쪽 이동
            j -= 1

    return ''.join(reversed(lcs_chars))

# 입력
X = input()
Y = input()

print(lcs_length(X, Y)) # LCS 길이 출력
print(lcs_string(X, Y)) # LCS 문자열 출력