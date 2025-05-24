import sys

def dfs(input):
    n = int(input[0])  # ex) 9
    original = n
    count = 0

    temp_sum = None  # while문 최초 진입 위해 None 설정

    print(f"시작값: {n}")
    
    while temp_sum != original:
        if temp_sum is None:
            temp_sum = n

        count += 1

        if temp_sum >= 10:
            one = temp_sum % 10
            two = temp_sum // 10
            digit_sum = one + two
            temp_sum = (one * 10) + (digit_sum % 10)
        else:
            temp_sum = (temp_sum * 10) + (temp_sum)

        print(f"[{count}회차] 새 수: {temp_sum}")

    print(f"총 사이클 수: {count}")

if __name__ == '__main__':
    input = sys.stdin.read().splitlines()
    dfs(input)