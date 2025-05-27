# 색종이 만들기 2630번

def divide(x, y, size, count):
    color = paper[x][y]
    sameColor = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                sameColor = False
                break
        if not sameColor:
            break
    
    if sameColor:
        count[color] += 1
        return

    half = size // 2
    divide(x, y, half, count)
    divide(x + half, y, half, count)
    divide(x, y + half, half, count)
    divide(x + half, y + half, half, count)

if __name__ == "__main__":
    from sys import stdin

    input = stdin.readline

    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    count = [0, 0]

    divide(0, 0, N, count)

    print(count[0])
    print(count[1])