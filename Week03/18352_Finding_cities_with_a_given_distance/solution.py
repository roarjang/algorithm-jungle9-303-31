# 문제: https://www.acmicpc.net/problem/18352
# 날짜: 2025-06-05
# 난이도: SILVER II

# 문제 핵심
# x에서 출발해 BFS를 돌리면, 거리 순으로 탐색됨
# 각 도시마다 거리를 배열에 저장하면서
# 거리 K인 도시만 결과 리스트에 넣고 출력

from sys import stdin
from collections import deque
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 풀이 코드 작성

# 입력 및 초기화
N, M, K, X = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 배열 초기화
distance = [-1] * (N + 1)
distance[X] = 0 # 시작 도시는 거리 0

# BFS
queue = deque([X])
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1: # 방문하지 않은 도시라면
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

# 결과 출력
found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)