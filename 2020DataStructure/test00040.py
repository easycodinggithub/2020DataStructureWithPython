Num = int(input())
for i in range(2, int(Num ** 0.5) + 1):
    if Num % i == 0:
        continue
    else:
        print("소수 입니다.")
        exit()
print("소수가 아닙니다.")

