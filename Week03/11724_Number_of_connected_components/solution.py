# 문제: https://www.acmicpc.net/problem/11724
# 날짜: 2025-06-05
# 난이도: SILVER II

from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**6)

stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 요약
# 입력
    # 정점 개수 N(1 <= N <= 1,000)
    # 간선 개수 M
    # 이어진 정점 쌍 M개
# 출력
    # 연결 요소 (Connected Component)의 개수

# 핵심 아이디어
# 그래프는 인접 리스트 또는 인접 행렬로 표현
# 모든 정점을 순회하면서, 아직 방문하지 않은 정점이면
    # DFS/BFS를 한 번 돌리고, 카운트 1증가
# 즉, DFS/BFS 한 번 = 하나의 연결 요소

# 문제 풀이 코드 작성

# 인접리스트 + BFS
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        for next_node in graph[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# 입력
N, M = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프

# 연결 요소 개수 세기
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, visited, i)
        count += 1

print(count)