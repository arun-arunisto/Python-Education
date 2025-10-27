# copy()
print("copy".center(20, "*"))
a = [[1, 2], [3, 4]]
b = a
print(a)
b[0] = [1, 2, 3]
print(a)   
print("-".center(20, "*"))

print("shallow copy".center(20, "*"))
# shallow copy
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
print(a)
b[0] = [1, 2, 3]
print(a)
print(b)
b[1][0] = 99
print(a)
print(b)
print("-".center(20, "*"))

print("deep copy".center(20, "*"))
# deep copy
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
print(a)
b[0] = [1, 2, 3]
print(a)
print(b)
b[1][0] = 99
print(a)
print(b)
print("-".center(20, "*"))
