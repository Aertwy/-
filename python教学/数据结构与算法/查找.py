#顺序查找


"""
def order (search,list1):
    i = list1.index(search)
    return list1[i]
list1 = [0,1,2,3,4,5,"你",8,9,10]
order("你",list1)
时间复杂度为O(n)
"""
"""
def order (search, list1):
    for i,o in enumerate(list1):
        if search==o:
            return i
    return -1
"""
#list1 = [0, 1, 2, 3, 4, 5, "你", 8, 9, 10]
def two_minutes(num,list2):
#初始化
    left = 0
    right = len(list2)-1
    while left <= right:
        mid = (left + right) // 2
        if list2[mid] == num:
            return mid
        elif num < list2[mid]:
            right = mid - 1
        elif num > list2[mid]:
            left = mid + 1
    else: return -1

list2 = [0,1,2,3,4,5,6,7,8,9,10]
print(two_minutes(0, list2))
print(two_minutes(10, list2))
print(two_minutes(15, list2))

















































































