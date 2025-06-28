# 문제: https://www.acmicpc.net/problem/24480
# 날짜:2025-06-28
# 난이도: SILVER II
# 문제유형: DFS

# 문제 설명
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프
# 정점 번호는 1번부터 N번, 간선의 가중치는 1
# 깊이 우선 탐색으로 방문 (인접 정점은 내림차순으로)

# 핵심 아이디어


# 입력
# 정점 N(5 <= N <= 100,000), 간선 M (1 <= M <= 200,000)
# 시작 정점 R (1 <= R <= N)
# 간선 정보 (u, v) / v의 가중치 1인 양방향 간선

# 출력

# 시간복잡도
# 보통은 입력 정렬 없이 O(n + m)으로 간주되며,
# 이 문제처럼 정렬 조건이 있다면 O(m log m + n)

# 공간복잡도
# 그래프 + visited = O(n + m) + O(n)
# = O(n + m)


from typing import List
import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

def read_input() -> tuple[int, int, int, List[List[int]]]:
    input = lambda: sys.stdin.readline().strip()
    n, m, r = map(int, input().split())
    # 공간복잡도: [입력 그래프 저장] 인접 리스트 방식
    # 최대 2 * m개의 간선 저장 -> O(n + m)
    graph = [[] for _ in range(n + 1)]

    # 시간복잡도: [입력처리] m개의 간선을 읽고 양쪽에 추가 -> O(m)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 시간복잡도: [인접 리스트 정렬] 각 리스트의 길이 합은 총 간선 수의 2배 (양방향)
    # O(m log m)
    for adj in graph:
        adj.sort(reverse=True)

    return n, m, r, graph

def dfs(node: int, graph: List[List[int]],
        visited: List[int], counter: List[int]) -> None:
    visited[node] = counter[0]
    counter[0] += 1

    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            # 시간복잡도: [DFS 재귀 호출] 모든 정점 1회 방문, 모든 간선 1회 탐색
            # O(n + m)
            # 공간복잡도: [재귀 호출 스택] DFS의 최대 호출 깊이는 최악의 경우 n까지 가능
            # 재귀 스택 공간: O(n)
            dfs(neighbor, graph, visited, counter)

def solve(n: int, r: int, graph: List[List[int]]) -> List[int]:
    # 공간복잡도: [방문 리스트] -> O(n + 1)
    visited = [0] * (n + 1)
    # 공간복잡도: [재귀 공유 리스트] -> 고정 크기 O(1)
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