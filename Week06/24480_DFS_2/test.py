from typing import List
import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def read_input() -> tuple[int, int, int, List[List[int]]]:
    input = lambda: sys.stdin.readline().strip()

    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 인접 리스트 내림차순 정렬 (전처리)
    for adj in graph:
        adj.sort(reverse=True)

    return n, m, r, graph

def dfs(node: int, graph: List[List[int]],
        visited: List[int], counter: List[int]) -> None:
    visited[node] = counter[0]
    counter[0] += 1

    for neighbor in graph[node]:
        if (visited[neighbor] == 0):
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