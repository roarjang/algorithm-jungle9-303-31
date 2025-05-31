# 문제: https://www.acmicpc.net/problem/2606
# 날짜: 2025-06-01
# 난이도: Silver III

from sys import stdin
from collections import deque
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 인접 리스트 + BFS
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        cur = queue.popleft()
        for next_node in graph[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                count += 1
    
    return count

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    V = 1

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    count = bfs(graph, visited, V)
    print(count)

# # 문제 풀이 코드 작성 [BFS]

# def bfs(graph, visited, start):
#     queue = deque([start])
#     visited[start] = True
#     count = 0

#     while queue:
#         cur = queue.popleft()
        
#         for next_node in range(1, N + 1):
#             if not visited[next_node] and graph[cur][next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#                 count += 1 # start 정점 제외한 감연된 컴퓨터 수를 count!
    
#     return count

# if __name__ == "__main__":
#     # 입력 및 초기화
#     N = int(input())
#     M = int(input())
#     V = 1

#     graph = [[False] * (N + 1) for _ in range(N + 1)]
#     visited = [False] * (N + 1)

#     # 그래프 정보 입력
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a][b] = True
#         graph[b][a] = True

#     # BFS
#     count = bfs(graph, visited, V)
#     print(count)

# # 문제 풀이 코드 작성 [DFS]

# def dfs(idx):
#     global visited, count
#     visited[idx] = True

#     for next in range(1, N + 1):
#         if not visited[next] and graph[idx][next]:
#             count += 1
#             dfs(next)

# if __name__ == "__main__":
#     # 0. 입력 및 초기화
#     N = int(input())
#     M = int(input())
#     V = 1

#     graph = [[False] * (N + 1) for _ in range(N + 1)]
#     visited = [False] * (N + 1)
#     count = 0

#     # 1. 그래프 정보 입력
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a][b] = True
#         graph[b][a] = True

#     # 2. dfs
#     dfs(V)
#     print(count)