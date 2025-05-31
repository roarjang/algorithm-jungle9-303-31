# 문제: https://www.acmicpc.net/problem/1260
# 날짜: 2025-06-01
# 난이도: Silver II

from sys import stdin, stdout
from collections import deque
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()


# 문제 풀이 코드 작성
def dfs(graph, visited, V):
    visited[V] = True
    print(V, end = ' ')

    for next_node in range(1, N + 1):
        if not visited[next_node] and graph[V][next_node]:
            dfs(graph, visited, next_node)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')

        for next_node in range(1, N + 1):
            if not visited[next_node] and graph[cur][next_node]:
                visited[next_node] = True
                queue.append(next_node)

if __name__ == "__main__":
    # 입력 및 초기화
    N, M, V = map(int, input().split())

    # 인접 행렬로 그래프 초기화
    graph = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True

    # DFS
    visited = [False] * (N + 1)
    dfs(graph, visited, V)
    print()

    # BFS
    visited = [False] * (N + 1)
    bfs(graph, visited, V)