# 수 정렬하기 2

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 퀵 정렬 (divide and conquer 알고리즘)
N = int(input())

arr = [int(input() for _ in range(N))]

# 1. 기준값(Pivot)을 하나 정함
# 2. Pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할
# 3. 왼쪽과 오른쪽을 재귀적으로 정렬

def quick_sort_inplace(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽에서 pivot보다 큰 값 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 오른쪽에서 pivot보다 작은 값 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할된 영역 재귀 호출
    quick_sort_inplace(arr, start, right - 1)
    quick_sort_inplace(arr, right + 1, end)


