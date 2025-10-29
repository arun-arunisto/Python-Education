# Generator
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i+=1
counter = count_up_to(3)
print(next(counter)) # 0
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
#print(next(counter)) # StopIteration
    
# list vs generator
import sys

num_list = [x for x in range(1000)]
num_gen = (x for x in range(1000))

print(sys.getsizeof(num_list)) # large memory
print(sys.getsizeof(num_gen)) # small memory footprint

# num_gen is not a tuple it's a generator
"""
if it's comma seperated value it's tuple
if there's any experssion (for) it's a generator
"""
