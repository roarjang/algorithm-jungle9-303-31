# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 
# 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 
# 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# <!-- 내장 함수 사용 -->
# from math import gcd

# a, b = map(int, input().split())
# print(gcd(a, b))
# print((a * b) // gcd(a, b))

# <!-- GCD 함수로 구현 -->

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# <!-- GCD 구현 -->

# if __name__ == "__main__":
#     from sys import stdin

#     input = stdin.readline

#     x, y = map(int, input().split())

#     a, b = x, y

#     # 유클리드 호제법
#     while y:
#         x, y = y, x % y

#     gcd = x # Greatest Common Divisor, 최대 공약수
#     lcm = (x * y) // gcd # Lowest Common Multiple, 최소 공배수

#     print(gcd)
#     print(lcm)