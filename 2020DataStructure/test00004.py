# 문자열 입력하기
# name = input("이름을 입력하세요 : ") # 문자열 입력받기
# print("My name is", name) # , 로 문자열 연결 ( 숫자, 문자 모두 연결 )
# print("My name is" + name) # + 로 문자열 연결 ( 문자만 연결 )
# # ctrl + shift + f10
#
# a = input('a = ') # 문자열 입력받기
# b = input('b = ')
#
# a = int(a) # 문자열을 정수로 변환
# b = int(b)
#
# # a = int(input('a = ')) # 이 형태로 보통 사용
#
# print('-' * 10) # - 기호 10회 반복 출력
# print(a + b) # 두 숫자 더하여 출력하기
# print('-' * 10)

Num1 = int(input('첫 번째 숫자 : '))

Num2 = int(input('두 번째 숫자 : '))

print('두 숫자의 합 :', Num1 + Num2)
print('두 숫자의 차 :', Num1 - Num2)
print('두 숫자의 곱 :', Num1 * Num2)
print('두 숫자의 몫 :', Num1 / Num2)

print(f'두 숫자의 합 : {Num1 + Num2}')