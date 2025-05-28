# 문제: https://www.acmicpc.net/problem/1629
# 날짜: 2025-05-28
# 난이도: Silver I

from sys import stdin, stdout
stdin = open('input.txt', 'r')

# 문제 풀이 코드 작성
def fastExponentiation(a, b, c): # a^b % c 계산 (빠른 거듭제곱)
    # 기저 조건: 지수가 1이면 a % C 반환
    if b == 1:
        return a % c
    
    # 지수를 반으로 나누어 재귀 호출
    half = fastExponentiation(a, b // 2, c)

    if b % 2 == 0: # 지수가 짝수인 경우: (a^b) = (a^(b // 2))^2
        return (half * half) % c
    else: # 지수가 홀수인 경우: (a^b) = (a^(b // 2))^2 * a
        return (half * half * a) % c

if __name__ == "__main__":
    input = stdin.readline

    A, B, C = map(int, input().split())
    print(fastExponentiation(A, B, C))