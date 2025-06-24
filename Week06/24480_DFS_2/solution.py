# 문제: https://www.acmicpc.net/problem/24480
# 날짜:2025-06-24
# 난이도: SILVER II
# 문제유형: DFS

# 문제 설명
# N개의 정점과 M개의 간서으로 구성된 무방향 그래프
# 정점 번호는 1번부터 N번, 간선의 가중치는 1
# 깊이 우선 탐색으로 방문 (인접 정점은 내림차순으로)

# 핵심 아이디어


# 입력
# 정점 N(5 <= N <= 100,000), 간선 M (1 <= M <= 200,000)
# 시작 정점 R (1 <= R <= N)
# 간선 정보 (u, v) / v의 가중치 1인 양방향 간선

# 출력

# 시간복잡도


# 공간복잡도


from typing import List
import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def read_input() -> tuple[int, int, int, List[List[int]]]:
    input = sys.stdin.readline
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort(reverse=True)

    return n, m, r, graph

def dfs(node: int, graph: List[List[int]],
        visited: List[int], counter: List[int]) -> None:
    visited[node] = counter[0]
    counter[0] += 1

    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor, graph, visited, counter)

def solve(n: int, r: int, graph: List[List[int]]) -> List[int]:
    visited = [0] * (n + 1)
    counter = [1]
    dfs(r, graph, visited, counter)

    return visited

def main():
    n, m, r, graph = read_input()
    visited = solve(n, r, graph)

    for i in range(1, n + 1):
        print(visited[i])

if __name__ == "__main__":
    main()