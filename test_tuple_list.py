a = ("我", "最", "帅",)
a = a[0:1] + ("是",) + a[1:] + ("的",)
for i in a:
    print(i)

b = ["1", "2", "3"]

c = [1,2,3]+[1,5,6]
print(b.pop(-1),c)

s = "ajldjlajfdljfddd"

print("".join(sorted(set(s))))

import keyword

dir(keyword)
print(dir())