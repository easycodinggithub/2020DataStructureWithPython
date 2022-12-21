# 문제 Kim 이라는 매개변수 값을 넘겨줄 때
# 'Hi, Kim' 이 출력되도록 하시오

def Hello(name):
    print('Hi,', name)

Hello('Kim')

def info(name, address, phone):
    print(f'제 이름은 {name}이고, 주소는 {address}입니다. 제 전화번호는 {phone}입니다')

info('김동균', '대구소프트웨어고등학교', '1023192032')

def Singer(A, B, C):
    print(f'저가 좋아하는 가수 3명은 {A}, {B}, {C}입니다')

A = input('내가 좋아하는 첫번째 가수는 : ')
B = input('내가 좋아하는 두번째 가수는 : ')
C = input('내가 좋아하는 세번째 가수는 : ')

Singer(A, B, C)