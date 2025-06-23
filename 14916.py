#거스름돈
n = int(input())

#돈은 2원과 5원이 있음 
coins = [2,5]

#dp테이블 생성
INF = 100001
dp = [INF] * (n+1)

#0번째는 0으로 초기화 한다
dp[0] = 0

#코인 한개마다 전체 dp테이블을 돈다.
for coin in coins:
    for i in range(2,n+1):
        #100001보다 작은 숫자라면 
        if dp[i-coin] < INF:
            dp[i] = min(dp[i - coin] + 1, dp[i])

# print(dp)

#INF로 설정해놓았던 숫자라면 거스름돈을 줄 수 없으므로 -1를 프린트
if dp[n] == INF:
    print(-1)

else: 
    print(dp[n])