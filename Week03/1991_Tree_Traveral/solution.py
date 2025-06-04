# 문제: https://www.acmicpc.net/problem/1991
# 날짜: 2025-06-05
# 난이도: Silver I

from sys import stdin, stdout
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 풀이 코드 작성

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':
        return ''
    return node + preorder(tree[node][0]) + preorder(tree[node][1])

# 중위 순회: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return ''
    return inorder(tree[node][0]) + node + inorder(tree[node][1])

# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return ''
    return postorder(tree[node][0]) + postorder(tree[node][1]) + node

# 입력 및 초기화
N = int(input())

# 트리 딕셔너리 자료형으로 초기화
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

# 루트는 항상 "A"
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))