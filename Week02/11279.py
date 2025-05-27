# 11279 - 최대 힙

# 문제
# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 
# 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
# x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
# 입력되는 자연수는 231보다 작다.

# 출력
# 입력에서 0이 주어진 횟수만큼 답을 출력한다. 
# 약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

if __name__ == "__main__":
    import heapq
    from sys import stdin, stdout

    input = stdin.readline
    heap = []
    output = []

    N = int(input())

    for i in range(N):
        cmd = int(input())

        if cmd > 0:
            # 최대 힙처럼 사용하기 위해 -cmd push
            heapq.heappush(heap, -cmd)
        elif cmd == 0:
            if heap:
                # 꺼낸 후 부호를 다시 바꿔 출력
                output.append(-heapq.heappop(heap))
            else:
                output.append(0)

    stdout.write("\n".join(map(str, output)))

# 부모, 왼쪽 자식, 오른쪽 자식 인덱스를 구하는 유틸 함수
# def parent(i):
#     return (i - 1) // 2

# def left(i):
#     return (2 * i) + 1

# def right(i):
#     return (2 * i) + 2

# heappush: 힙에 원소를 추가하고, 위로 올라가며 정렬(sift-up)
# def heappush(heap, x):
#     heap.append(x) # 값을 맨 뒤에 삽입
#     i = len(heap) - 1 # 삽인된 위치의 인덱스

#     # sift up (부모보다 작으면 위로 올라가며 swap)
#     while i > 0:
#         p = parent(i)
#         if heap[i] < heap[p]: # 최소 힙 조건: 자식 < 부모
#             heap[i], heap[p] = heap[p], heap[i]
#             i = p
#         else:
#             break

# heappop: 힙에서 최소값(루트)을 꺼내고, 마지막 값을 위에 올린 뒤 아래로 내려가며 정렬(sift-down)
# def heappop(heap):
#     if not heap:
#         raise IndexError("heappop from empty heap")
    
#     min_val = heap[0] # 루트 최소값 (최소값)을 꺼냄
#     last_val = heap.pop() # 마지막 값을 꺼냄

#     if heap:
#         heap[0] = last_val # 마지막 값을 루트에 놓고
#         i = 0

#         # sift down (자식 중 더 작은 쪽과 비교하며 아래로 내려감)
#         while True:
#             li, ri = left(i), right(i)
#             smallest = i

#             # 왼쪽 자식이 더 작으면 교체 대상
#             if li  < len(heap) and heap[li] < heap[smallest]:
#                 smallest = li

#             # 오른쪽 자식이 더작으면 교체 대상
#             if ri < len(heap) and heap[ri] < heap[smallest]:
#                 smallest = ri

#             if smallest == i:
#                 break # 더 이상 내려갈 필요 없음

#             heap[i], heap[smallest] = heap[smallest], heap[i]
#             i = smallest
    
#     return min_val

# if __name__ == "__main__":
#     from sys import stdin, stdout

#     input = stdin.readline
#     heap = [] # 내부 최소 힙
#     output = []

#     N = int(input())

#     for i in range(N):
#         cmd = int(input())

#         if cmd > 0:
#             heappush(heap, -cmd)
#         elif cmd == 0:
#             if len(heap) == 0:
#                 output.append(0)
#             else:
#                 output.append(-heappop(heap))

#     stdout.write('\n'.join(map(str, output)))