fi = [[0,0],[1,1],[2,2],[0,1],[0,2]]
if (all([0, y] in fi for y in range(3))
        or

        all(y in fi for y in fi)):
    print("可以")

print(all([x, x] in fi for x in range(3)))
print(all([0, y] in fi for y in range(3)))

for x, y in enumerate(range(2, -1, -1)):
    print(x, y)      # (0,2) (1,1) (2,0)，x 自动正序，y 是倒序



































