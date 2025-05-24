# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# 예제 입력 1 
# 6
# 20 1 15 8 4 10
# 예제 출력 1 
# 62

N = int(input())
data = list(map(int, input().split()))

arr = [1, 2, 3]
visited = [False] * len(arr)
current = [] # 지금까지 고른 숫자들을 저장하는 리스트 -> 즉, 순열을 만들어가는 중간 상태

def permute(arr, visited, current):
    if len(current) == len(arr): # 현재 만든 순열이 arr와 같은 길이가 되면 순열 하나 완성
        print(current)
        return # 완성된 순열 출력 + 더 이상 깊이 들어가지 않고 재귀 종료
    
    for i in range(len(arr)):
        if not visited[i]: # 이 숫자 arr[i]가 아직 선택되지 않았으면 (중복 방지 조건)
            visited[i] = True # 숫자 선택 -> 사용 표시
            current.append(arr[i]) # 지금 고른 숫자를 순열의 다음 자리에 넣음
            permute(arr, visited, current) # 다음 숫자 
            current.pop()
            visited[i] = False

permute(arr, visited, [])