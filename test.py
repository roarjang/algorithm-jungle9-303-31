# 피보나치 수열
def fib(n):
    dp = [0] * (n + 1)
    if n>= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 그리디 알고리즘 - 거스름돈
def greedy_coin(change, coins):
    coins.sort(reverse = True)
    count = 0
    for coin in coins:
        if change >= coin:
            count += change // coin
            change %= coin
    return count

# 단점: 항상 최적해를 보장하진 않음 (동정 종류가 1, 3, 4원일 때 6원을 그리디로는 최적해 못 찾음)

# DFS / BFS - 미로 최단 경로 (BFS)
from collections import deque

def bfs_maze(maze, start, end):
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)]) # (x, y, distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

# 위상 정렬 - 예시: Kahn's Algorithm
from collections import deque

def topological_sort(n, edges):
    indegree = [0] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else [] # 사이클이 있을 경우 빈 리스트

# 다익스트라 알고리즘 (최단 거리: 1 -> N)
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)] # (거리, 노드)

    while heap:
        cur_dist, u = heapq.heappop(heap)
        if cur_dist > dist[u]:
            continue
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))
    return dist

# 플로이드 워셜 (모든 정점 간 최단 거리)
def floyd_warshall(n, graph):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# 최소 신장 트리 - 크루스칼 알고리즘
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2]) # 가중치 기준 정렬
    parent = list(range(n))
    total_cost = 0

    for u, v, cost in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += cost

    return total_cost

# 힙 (최소 힙, 삽입/삭제)
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

print(heapq.heappop(heap))

# 트라이 (Trie) 구현
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.is_end = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.is_end