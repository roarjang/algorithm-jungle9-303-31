# 문제: LeetCode (1578) Minimum Deletion Cost (Repeat Letters)
# 날짜: 2025-06-06
# 난이도: 기초 (하)

# 문제 핵심
# 연속된 문자가 있으면 더 작은 비용의 문자를 삭제하는 방식

# 시간 복잡도: O(N)
# 공간 복잡도: O(1)

from sys import stdin, stdout
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

# 문제 풀이 코드 작성
from typing import List

def min_cost(s: str, cost: List[int]) -> int:
    if len(s) <= 1:
        return 0 # 한 글자 이하면 삭제할 필요 없음
    
    total_cost = 0
    prev_char = s[0]
    max_cost = cost[0]

    for i in range(1, len(s)):
        curr_char = s[i]
        curr_cost = cost[i]

        if curr_char == prev_char:
            # 중복 문자가 연속된 경우, 더 적은 비용을 누적하고
            # 더 큰 비용을 남겨서 살린다
            total_cost += min(curr_cost, max_cost)
            max_cost = max(curr_cost, max_cost)
        else:
            # 문자가 바뀌면 새로운 그룹 시작
            prev_char = curr_char
            max_cost = curr_cost

    return total_cost

# 입력
s = input()
cost = list(map(int, input().split()))

# 출력
print(min_cost(s = s, cost = cost))