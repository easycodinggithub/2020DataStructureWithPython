from math import gcd
Num1, Num2 = map(int, input().split())
print(f"최대 공약수 : {gcd(Num1, Num2)}, 최소 공배수 : {Num1*Num2 / gcd(Num1, Num2)}")