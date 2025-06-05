# 문제: Maximum Units on a Truck (LeetCode 1710)
# 날짜: 2025-06-05
# 난이도: 기초 (하)

# 예제 입력 처리
from sys import stdin
stdin = open('input.txt', 'r')
input = lambda: stdin.readline().strip()

from typing import List

# 문제 풀이 코드 작성
def maximum_units(box_types:List[List[int]], truck_size:int) -> int:
    # 내림차순으로 정렬 (유닛이 많이 들어 있는 박스 우선순위)
    box_types.sort(key = lambda box:box[1], reverse = True)

    # 트럭 여유 공간, 총 유닛 카운트 초기화
    total_unit = 0
    space_left = truck_size

    for box_count, units_per_box in box_types:
        boxes_to_load = min(space_left, box_count)
        total_unit += boxes_to_load * units_per_box
        space_left -= boxes_to_load

        if space_left == 0:
            break

    return total_unit

box_info = [list(map(int, input().split())) for _ in range(4)]
print(maximum_units(box_info, 4))