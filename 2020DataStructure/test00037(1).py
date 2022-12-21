# 5 5
# 00110
# 00010
# 11111
# 00001
# 11100
# 3

n,m = map(int,input().split())
graph = [] #빈 리스트 생성
for i in range(n): #n줄만큼 입력받기
    graph.append(list(map(int,input()))) #split을 사용할 필요가 없다

def puddle(x,y): #물 웅덩이의 개수를 체크하는 함수
     if x<=-1 or x>=n or y <= -1 or y >= m:
         return False

     if graph[x][y] == 0:
         graph[x][y] = 1
         puddle(x - 1, y)
         puddle(x, y - 1)
         puddle(x + 1, y)
         puddle(x, y+1)
         return True
     else:
         return False

cnt = 0 #물 웅덩이 개수
for i in range(n):
     for j in range(m):
         if puddle(i,j) == True:
             cnt += 1

print(cnt)