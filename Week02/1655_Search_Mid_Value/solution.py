# 문제: https://www.acmicpc.net/problem/1655
# 날짜: 2025-05-29
# 난이도: GOLD II

from sys import stdin, stdout
import heapq
stdin = open('input.txt', 'r')

# 문제 풀이 코드 작성

if __name__ == "__main__":
    input = stdin.readline

    N = int(input())
    
    min_heap = [] # 중앙값 이하
    max_heap = [] # 중앙값 초과

    for i in range(N):
        num = int(input())

        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # 균형 맞추기: max_heap이 항상 min_heap보다 같거나 1개 많아야 함
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중앙값 출력
        print(-max_heap[0])