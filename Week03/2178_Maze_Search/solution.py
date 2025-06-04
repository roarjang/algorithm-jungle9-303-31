# 문제: https://www.acmicpc.net/problem/2178
# 날짜: 2025-06-05
# 난이도: SILVER I

# 문제 핵심 요약
# N줄 M열의 0과 1로 구성된 미로
# 시작점: (0, 0) (실제 좌표는 1,1 인데 코드에서는 0-indexed)
# 도착점: (N-1, M-1)
# 출력: 최단 거리

from sys import stdin
from collections import deque
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 풀이 코드 작성
# 이동 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 벗어나면 스킵
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽이거나 이미 방문한 곳이면 스킵
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue

            # 처음 방문하는 길이면 거리 갱신
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))

    return graph[N - 1][M - 1] # 도착지의 거리 값 반환

# 입력 및 초기화
N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)] # 미로 저장
visited = [[False] * (M) for _ in range(N)]

print(bfs(0, 0))