# 18258 - 큐 2

# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

if __name__ == "__main__":
    # import sys
    from sys import stdin, stdout
    from collections import deque

    input = stdin.readline
    q = deque([])
    output = []

    N = int(input())

    for _ in range(N):
        # .strip(): 문자열의 양쪽 공백과 개행 문자 제거
        # .split(): 공백 기준으로 명령어와 숫자 분리
        command = input().strip().split()
        cmd = command[0]

        if cmd == "push":
            q.append(int(command[1]))
        elif cmd == "pop":
            output.append(q.popleft() if q else -1)
        elif cmd == "size":
            output.append(len(q))
        elif cmd == "empty":
            output.append(0 if q else 1)
        elif cmd == "front":
            output.append(q[0] if q else -1)
        elif cmd == "back":
            output.append(q[-1] if q else -1)
        
    # 한 번에 출력
    # 'separator'.join(iterable)
    stdout.write('\n'.join(map(str, output)))

# <-- Queue 자료구조를 만들어서 풀이했는데, 
# pop(0)으로 할 경우 인덱스에 요소를 제거하고 뒤쪽에 요소를 한 칸씩 이동하므로
# 시간복잡도가 O(N)이 된다.
# loop와 중첩이 되면 O(N^2)이 되므로 시간초과 발생함-->

# class MyQueue:
#     def __init__(self):
#         self.data = []

#     def push(self, x):
#         self.data.append(x) # 뒤에 추가 (enqueue)

#     def pop(self):
#         if self.empty():
#             return -1
#         return self.data.pop(0) # 앞에서 제거
    
#     def size(self):
#         return len(self.data)
    
#     def empty(self):
#         return 1 if len(self.data) == 0 else 0
    
#     def front(self):
#         if self.empty():
#             return - 1
#         return self.data[0]
    
#     def back(self):
#         if self.empty():
#             return -1
#         return self.data[-1]

# if __name__ == "__main__":
#     import sys
    
#     input = sys.stdin.readline

#     q = MyQueue()

#     N = int(input())

#     for i in range(N):
#         command = input().split()

#         if len(command) == 1:
#             if command[0] == "front":
#                 print(q.front())
#             elif command[0] == "back":
#                 print(q.back())
#             elif command[0] == "size":
#                 print(q.size())
#             elif command[0] == "empty":
#                 print(q.empty())
#             elif command[0] == "pop":
#                 print(q.pop())
#         elif len(command) == 2:

#             q.push(command[1])