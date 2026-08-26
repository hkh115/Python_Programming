a = "python"
print(a, type(a))
b = 'python'

print("I'll be back")
print('I\'ll be back')

multiline = """
Life is short
You need Python
"""
print(multiline)

def func():
    pass

print(func.__doc__)
print("Hello" + "Python")
print("Hello" * 10)
print("-" * 100)

print("Hello" + str(10))

print("10" + "2")

name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이 : {age + 1}")
print(f"{name.upper()}")

pi = 3.141592
print(f"{pi:.3f}")

num = 123456789
print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:<15d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
