a = input()
print(a)
print(type(a))

a = input()
a = int(a)
print(a, type(a))

a = int(input())

a = float(input())
print(a, type(a))

a = int(input())
b = int(input())
print(a, b)

a = input().split()
print(a, type(a))

a, b, c = map(int, input().split())
print(a, b, c, type(a))

a = list(map(int, input().split()))
print(a, type(a))
