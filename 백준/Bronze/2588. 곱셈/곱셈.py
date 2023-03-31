a = int(input())
b = int(input())
c = b // 100 ### 3
d = (b - (c * 100)) // 10 ###8
e = b - (c * 100) - (d * 10)

print(a * e)
print(a * d)
print(a * c)
print(a * b)