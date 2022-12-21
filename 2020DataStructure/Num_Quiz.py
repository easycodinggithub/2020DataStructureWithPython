Num_One = []
Num_Ten = []

N = int(input("몇 개의 숫자를 입력하겠습니까 : "))

for i in range(0, N):
    Number = int(input(f'{i + 1}번째 숫자 입력 :'))
    if Number >= 10:
        Num_Ten.append(Number)
    else:
        Num_One.append(Number)

Num_One.sort()
Num_Ten.sort()

Len_One = len(Num_One)
Len_Ten = len(Num_Ten)

Sum = 0

if Len_One % 2 == 0:
    T = (Len_One/2)-1
else:
    T = (Len_One/2)

for i in range(0, Len_One):
    if i <= int(T):
        Sum += Num_One[i]
    else:
        Sum += Num_One[i] * 10

if Len_Ten % 2 == 0 & Len_Ten > 2:
    T = (Len_Ten/2)+1
else:
    T = (Len_Ten/2)

for i in range(0, Len_Ten):
    if i < int(T):
        Sum += Num_Ten[i]
    else:
        Sum += Num_Ten[i] * 100

print(Sum)