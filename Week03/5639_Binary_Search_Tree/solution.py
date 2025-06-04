# 문제: https://www.acmicpc.net/problem/5639
# 날짜: 2026-06-05
# 난이도: GOLD IV

from sys import stdin, setrecursionlimit
stdin = open('input.txt', 'r')
setrecursionlimit(10**9)
input = lambda: stdin.readline().strip()

# 문제 요약
# 입력: 전위 순회 결과가 줄마다 주어짐 (노드 값: 정수)
# 출력: 후위 순회 결과를 줄마다 출력

# 핵심 아이디어
# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
# 이진 탐색 트리의 성질을 이용하면 전위 순회 결과로부터 트리를 재구성할 수 있음

# 풀이 순서
# 1. 전위 순회 결과를 리스트로 받음
# 2. 재귀적으로 다음을 수행
#    - 리스트의 첫 번째 값을 루트로 설정
#    - 그보다 작은 값들 -> 왼쪽 서브트리
#    - 그보다 큰 값들 -> 오른쪽 서브트리
# 3. 위 구조를 기반으로 후위 순회 결과를 재귀적으로 구함

# 문제 풀이 코드 작성

# 입력전위 순회 결과 받기
preorder = []
for line in stdin:
    if line.strip():
        preorder.append(int(line))

# 후위 순회 함수 정의
def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]

    # 왼쪽 서브트리의 끝 찾기
    mid = start + 1
    while mid <= end and preorder[mid] < root:
        mid += 1

    postorder(start + 1, mid - 1) # 왼쪽 서브트리
    postorder(mid, end) # 오른쪽 서브트리
    print(root)

# 트리 전체에 대해 후위 순회 수행
postorder(0, len(preorder) - 1)