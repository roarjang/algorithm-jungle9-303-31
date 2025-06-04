# 문제: https://www.acmicpc.net/problem/2252
# 날짜: 2025-06-05
# 난이도: GOLD III

from sys import stdin
from collections import deque
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 핵심
# 학생 N명(1 ~ N번)이 있음
# M개의 정보가 주어짐: "A는 B보다 앞에 서야 한다" (A -> B)
# 이 조건을 모두 만족하는 학생들의 줄 세우기 순서를 출력

# 조건
# 순서를 여러 개 만들 수 있는 경우도 있으므로 정답이 여러 개일 수 있음
# 단, 사이클이 없다는 보장이 있음 (그래서 위상 정렬 가능)

# 핵심 개념: 위상 정렬이란?
# 방향 그래프에서 사이클이 없는 경우, 노드 간 순서 관계를 정리하는 알고리즘
# 학생 = 노드
# "앞에 서야 한다" 방향 간선
# 모든 조건을 만족하도록 순서대로 나열

# 문제 풀이 코드 작성

# 입력 및 초기화
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0인 노드부터 시작
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 위상 정렬 수행
result = []
while queue:
    current = queue.popleft()
    result.append(current)

    for next_node in graph[current]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

print(*result)