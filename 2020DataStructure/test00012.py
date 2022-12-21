import random # 랜덤 모듈
arr = list() # arr을 리스트로 선언
print(arr) # 빈 리스트 출력 , []

# 로또 번호 생성기
for i in range(6): # 10회 반복
    arr.append(random.randint(1, 46))

print(arr)

arr.sort()

print(arr[-2])