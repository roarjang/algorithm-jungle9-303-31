# 문제: https://www.acmicpc.net/problem/1992
# 날짜: 2025-5-28
# 난이도: Silver I

from sys import stdin, stdout
stdin = open('input.txt', 'r')

# 문제 풀이 코드 작성
# 영상이 섞여 있는 경우, 분할
def divide(x, y, size):
    base_video = arr[x][y]

    if is_same_video(x, y, size, base_video):
        output.append(str(base_video)) # int -> str로 바로 처리
        return
    
    half = size // 2

    output.append("(")

    divide(x, y, half)
    divide(x, y + half, half)
    divide(x + half, y, half)
    divide(x + half, y + half, half)

    output.append(")")

# 영상 판별하는 함수
def is_same_video(x, y, size, base_video):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != base_video:
                return False
            
    return True

if __name__ == "__main__":
    input = stdin.readline

    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    output = []

    divide(0, 0, N)

    stdout.write("".join(output))