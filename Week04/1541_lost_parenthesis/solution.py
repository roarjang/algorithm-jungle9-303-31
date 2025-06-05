# 문제: https://www.acmicpc.net/problem/1541
# 날짜: 2025-06-06
# 난이도: SILVER II
# 문제유형: Greedy (탐욕법)

# 문제 핵심
# 양수, 부호(+, -)가 있는 연산 식에 괄호를 이용하여 식의 값을 최소로 만들기 

# 그리디 알고리즘을 선택한 이유
# 뺄셈(-) 이후에 나오는 숫자들을 모두 괄호로 묶어 한꺼번에 빼는 것이,
# 전체 값을 최소로 만드는 최적의 전략이다.
# 이는 더 큰 수들을 최대한 한 번에 빼기 위해,
# 첫 뺄셈 이후의 모든 덧셈 그룹을 하나로 묶는 그리디 전략이다.

# 입력
# 1. 식은 '0'~'9', '+', '-'만으로 이루어져 있음
# 2. 가장 처음과 마지막 문자는 숫자
# 3. 연속해서 두 개 이상의 연산자가 나타나는 경우 X
# 4. 5자리를 초과하는 숫자 X
# 5. 수는 0으로 시작도 가능
# 6. 식의 문자열 길이는 50보다 작거나 같음

# 출력
# 최소값 출력 (0이하 정수도 가능)

# 시간복잡도
# 1. 숫자랑 부호 연산 리스트로 변경하기 -> 배열만큼 리스트 순회: O(N)
# 2. 연산 리스트를 연산하기 -> 배열만큼 리스트 순회: O(N)
# 최종 시간복잡도: O(N)

# 공간복잡도
# 연산 리스트 -> 배열만큼 공간 할당: O(N)

from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# Split 활용방식
def minimum_num(expression: str) -> int:
    # 1. '-' 기준으로 식을 나눈다.
    parts = expression.split('-')

    # 2. 첫 번째 그룹은 무조건 더한다.
    total = sum(map(int, parts[0].split('+')))

    # 3. 나머지 그룹은 각각 +로 쪼갠 뒤 더해서 전부 빼준다.
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))

    return total

# 입력
expression = input()

# 출력
print(minimum_num(expression))


# from sys import stdin
# stdin = open('input.txt', 'r')
# input = lambda: stdin.readline().strip()

# def minimum_num(tokens: str) -> int:
#     total = 0
#     minus_mode = False

#     for token in tokens:
#         if token == '-':
#             minus_mode = True
#         elif token == '+':
#             continue
#         else:
#             num = int(token)
#             if minus_mode:
#                 total -= num
#             else:
#                 total += num

#     return total

# # 입력: 숫자 + 연산자 나누기 (토큰 방식)
# expression = input()
# tokens = []
# curr = ""

# for char in expression:
#     if char in '+-' and curr:
#         tokens.append(curr)
#         tokens.append(char)
#         curr = ""
#     else:
#         curr += char

# if curr:
#     tokens.append(curr)

# # 출력
# print(minimum_num(tokens))