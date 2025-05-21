# 수 정렬하기

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5

N = int(input())

data = [int(input()) for _ in range(N)]

# 삽입 정렬
for i in range (1, N):
    key = data[i] # 현재 삽입할 값
    j = i - 1 # key 왼쪽부터 비교 시작

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j] # 한 칸씩 뒤로 밀기
        j -= 1 # <- 한 칸 왼쪽으로 이동

    data[j + 1] = key

for num in data:
    print(num)

arr = [1, 2, 3]

arr.sort()