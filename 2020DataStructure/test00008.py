# a = 5
# if a > 3:
#     print("a 는 3 보다 크다")
# elif a > 1:
#     print("a 는 3 보다 작고 1 보다 작다")
# else:
#     print("a 는 1 보다 작다")

# a, b = map(int, input().split())
#
# if a > b:
#     print(a)
# else:
#     print(b)

a = int(input())
if a > 70:
    print("최우수")
elif a > 50:
    print("우수")
elif a > 20:
    print("우수")
else:
    print("노력 필요")