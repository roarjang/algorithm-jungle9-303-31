# 이진트리 순회 (깊이 으순 탐색)

#    root(1)
#   2       3
#  4 5     6 7


# 전위순회 출력 : 1 2 4 5 3 6 7 (부 왼 오)
# 중위순회 출력 : 4 2 5 1 6 3 7 (왼 부 오)
# 후위순회 출력 : 4 5 2 6 7 3 1 (왼 오 부)

data = 0
lt = 0
rt = 0

def node(val):
    data = val
    lt = rt = None

root = 0

def dfs(root):
    