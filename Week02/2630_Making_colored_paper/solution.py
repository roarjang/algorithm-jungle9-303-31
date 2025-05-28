# 문제: https://www.acmicpc.net/problem/2630
# 날짜: 2025-05-27
# 난이도: Silver II

from sys import stdin
stdin = open('input.txt', 'r')

# 문제 풀이 코드 작성
# 분할하기
def divide(x, y, size, count):
    base_color = paper[x][y]
    if is_same_color(x, y, size, base_color):
        count[base_color] += 1
        return
    
    half = size // 2

    divide(x, y, half, count)
    divide(x + half, y, half, count)
    divide(x, y + half, half, count)
    divide(x + half, y + half, half, count)

# 동일한 색인지 확인하기
def is_same_color(x, y, size, base_color):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != base_color:
                return False
    return True

if __name__ == "__main__":
    input = stdin.readline

    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    count = [0, 0]

    divide(0, 0, N, count)

    print(count[0])
    print(count[1])