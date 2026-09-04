from this import s


for i in range(5):
    print(i, end = " ")


a = range(5)
print(a.start, a.stop, a.step)

for i in range(1, 6):
    print(i, end = " ")

for i in range(1, 11, 2):
    print(i, end = " ")

for i in range(5, 0, -1):
    print(i, end = " ")

tot = 0
for i in range(1, 11):
    tot += i
print(tot)

print(sum(range(1, 11)))


s = "한글asdkfh!@#"
for c in s:
    print(c, end = " ")
print(len(s))


for i in range (1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:<5d}", end = " ")
    print()
else:
    print("End")
