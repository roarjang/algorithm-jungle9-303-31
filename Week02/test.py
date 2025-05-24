# 🧩 예제 문제: 숫자 찾기

# 🔹 문제 설명

# 정렬된 수열 A가 주어졌을 때, 찾고자 하는 숫자 X가 수열 A에 존재하는지 확인하는 프로그램을 작성하세요. 존재하면 1, 존재하지 않으면 0을 출력합니다.

# 🔹 입력
# 	•	첫째 줄에 수열 A의 크기 N이 주어진다. (1 ≤ N ≤ 100,000)
# 	•	둘째 줄에 수열 A를 이루는 N개의 정수가 오름차순으로 주어진다.
# 	•	셋째 줄에 찾고자 하는 수 X가 주어진다. (1 ≤ X ≤ 1,000,000)

# 🔹 출력
# 	•	X가 A에 존재하면 1, 존재하지 않으면 0을 출력한다.

# 예제 입력
# 5
# 1 3 5 7 9
# 7

# 예제 출력
# 1

def binary_search(array, target, left, right):
    if left > right:
        return 0 # 못 찾음
    
    mid = (left + right) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, left, mid - 1)
    else:
        return binary_search(array, target, mid + 1, right)
    

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A.sort() # 정렬 필수

    X = int(input())

    print(binary_search(A, X, 0, len(A) - 1))