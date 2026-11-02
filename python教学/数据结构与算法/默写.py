"""
def b (num):
    while True:
        f = False
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                num[i],num[i+1] = num[i+1],num[i]
                f = True
        if not f:
            return num

test = [1,24,57,2,4,6879,32,576,879,321,45,678,3,8]

print(b(test))
"""

def c (num):
    for i in range(len(num)-1):
        min_index = i
        for j in range(i+1,len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i],num[min_index] = num[min_index],num[i]
    return num
test = [1, 24, 57, 2, 4, 6879, 32, 576, 879, 321, 45, 678, 3, 8]
print(c(test))
