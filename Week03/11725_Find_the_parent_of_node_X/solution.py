# 문제: https://www.acmicpc.net/problem/11725
# 날짜: 2025-06-05
# 난이도: SILVER II

from sys import stdin, stdout
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 핵심
# 루트가 1번인 트리가 주어졌을 때, 각 노드의 부모를 출력하기
# 입력
    # 첫 줄: 노드 수 N (2 <= N <= 100,000)
    # 다음 N - 1줄: 트리를 이루는 간선 정보 (u, v)
# 출력
    # 2번 노드부터 N번 노드까지, 각 노드의 부모 노드 번호

# 핵심 아이디어
# 트리는 사이클이 없는 연결 그래프
# 간선 정보로 인접 리스트를 구성
# 1번 노드에서 DFS 또는 BFS 탐색을 하며 방문한 노드의 부모 노드를 기록
# parent[2] ~ parent[N] 출력하면됨

# 왜 DFS/BFS로 풀이할까?
# 트리는 사이클이 없으므로, 한 번 방문한 노드는 무조건 자식이다.
# 따라서 탐색하면서 부모를 기록하면 정확하게 구분할 수 있다.

# 문제 풀이 코드 작성

# DFS로 부모 노드 찾기
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node # 현재 노드가 부모
            dfs(neighbor)

# 입력 및 그래프 초기화
N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [False] * (N + 1)

# 그래프 구성
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS로 부모 노드 찾기
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node # 현재 노드가 부모
            dfs(neighbor)

dfs(1) # 루트는 1번

# 2번부터 N번까지 출력
for i in range(2, N + 1):
    print(parent[i])