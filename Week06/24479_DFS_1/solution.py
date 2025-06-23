# 문제: https://www.acmicpc.net/problem/24479
# 날짜: 2025-06-23
# 난이도: SILVER II
# 문제유형: DFS

"""
문제 요약
- N개의 정점과 M개의 간선으로 구성된 무방향 그래프
- 정점 번호: 1 ~ N
- 간선은 중복 없이 주어짐
- DFS 탐색 시, 인접 정점은 오름차순으로 방문
- DFS 방문 순서를 출력 (시작 정점 R부터 시작, 방문 못하면 0 출력)
"""

# 시간복잡도
# O(N + M)

# 공간복잡도
# O(N + M)

# DFS 함수 정의
def dfs(node, graph, visited):
    global order
    # 현재 노드를 방문했다는 표시를 하며, 방문 순서를 기록
    # order = 3이면, node는 3번째로 방문된 노드라는 뜻
    visited[node] = order

    # 현재 노드(node)의 인접한 노드들을 하나씩 꺼내서
    for neighbor in graph[node]:
        # 아직 방문하지 않은 노드인 경우에만,
        # DFS는 한 번 방문한 노드는 다시 가지 않으니까 체크 필요
        if visited[neighbor] == 0:
            # 다음에 방문할 노드는 몇 번째 방문인지 순서를 미리 증가
            order += 1
            # 다음 노드를 재귀적으로 DFS 진행
            dfs(neighbor, graph, visited)

from sys import setrecursionlimit, stdin
stdin = open('input.txt', 'r')
# 재귀 깊이 제한 증가 (최악의 경우 100,000개 노드)
setrecursionlimit(10**6)

# 입력 처리: 정점 수, 간선 수, 시작 정점
N, M, R = map(int, input().split())

# graph 초기화: 인접 리스트 방식
graph = [[] for _ in range(N + 1)]

# 간선 정복 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프이므로 양쪽에 모두 추가

# 인접 정점 오름차순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 방문 순서 저장 배열 (0은 방문하지 않음)
visited = [0] * (N + 1)

# 방문 순서를 기록할 전역 변수
order = 1

dfs(R, graph, visited)

# 출력 (1번부터 N번까지 방문 순서 출력)
for i in range(1, N + 1):
    print(visited[i])