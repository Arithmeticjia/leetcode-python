def nums(a):
    if len(a) > 1:
        for i in range(1, len(a)):
            b = a[-i - 1:]
            num = b[0]
            print("b", b)
            b.sort()

            for j in range(len(b)):
                if b[j] > num:
                    b[j], b[0] = b[0], b[j]
                    print("num", num)
                    print("j", j)
                    min = b[0]
                    idx = j
                    for e in range(j+1, len(a)):
                        if num < a[e] < min:
                            min = a[e]
                            idx = e
                    print(min, idx)
                    a[j], a[idx] = a[idx], a[j]
                    print()
                    c = a[j+1:]
                    c.sort()
                    s = a[0:j+1] + c
                    print("s", s)
                    return s
    else:
        return a


a = []
n = 1234
print("原始数字", n)
# while n != 0:
#     a.append(n % 10)
#     n = int(n / 10)
a = [int(x) for x in str(n)]
print((a))
print(nums(a))
result = 0
for i in range(len(b) - 1, -1, -1):
    result = result * 10 + b[i]
print("result", result)
