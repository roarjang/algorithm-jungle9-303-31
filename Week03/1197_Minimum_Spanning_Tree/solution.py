# 문제: https://www.acmicpc.net/problem/1197
# 날짜: 2025-06-05
# 난이도: GOLD IV

from sys import stdin, stdout
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 요약
# 입력
    # 정점 V, 간선 E (1 <= V <= 10,000, 1 <= E <= 100,000)
    # 각 간선: A B C (정점 A, B를 가중치 C로 연결)
# 출력
    # 최소 신장 트리(MST)의 총 가중치

# MST 알고리즘 선택: Kruskal
# 간선 중심 알고리즘
# 간선을 가중치 기준으로 정렬한 후, 싸이클이 생기지 않도록 연결
# Disjoint Set (Union-Find) 자료구조 사용

# 문제 풀이 코드 작성
# 유니온-파인드
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        return True
    return False

# 입력
V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 가중치 기준 정렬
edges.sort()

# 유니온-파인드 초기화
parent = [i for i in range(V + 1)]

# 크루스칼 알고리즘
total_cost = 0
for cost, a, b in edges:
    if union(a, b):
        total_cost += cost

print(total_cost)