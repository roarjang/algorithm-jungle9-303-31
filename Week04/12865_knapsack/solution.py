# 문제: https://www.acmicpc.net/problem/12865
# 날짜: 2025-06-12
# 난이도: GOLD V
# 문제유형: DP

# 문제 설명
# 무게와 가치가 있는 물건을 배낭안에 넣어야 하는데,
# 배낭은 무게 제한이 있다.
# 무게 제한 내에 가치를 높일 수 있는 최대한 물건을 넣고
# 그 물건들의 가치합을 출력하자.

# 핵심 아이디어


# 입력
# 1. 물품의 수 N (1<= N <= 100)
# 2. 배낭 제한 무게 K (1 <= K <= 100,000)
# 3. 물품의 개수 만큼 각 물건의 무게 W와 물건의 가치 V
# (1 <= W <= 100,000), (0 <= V <= 1000)

# 출력
# 배낭에 넣을 수 있는 물건들의 가치합의 최대값 출력하기

# 시간복잡도


# 공간복잡도


from sys import stdin
stdin = open('input.txt', 'r')

input = lambda: stdin.readline().strip()

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)] # (무게, 가치)

# DP 테이블
dp = [[0] * (K + 1) for _ in range(n + 1)]

# DP 수행
for i in range(1, N + 1):
    weight, value = items[i - 1] # i번째 물건
    for w in range(K + 1):
        if weight > w:
            dp[i][w] = dp[i - 1][w] # 못 넣는 경우
        else:
            # 넣지 않는 경우 vs 넣는 경우 중 더 가치 큰 걸 선택
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

# 출력
print(dp[N][K]) # n개의 물건, k 무게일 때 최대 가치 