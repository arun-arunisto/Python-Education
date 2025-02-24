# Profiling using time module
"""
time() module is a simple way to measure execution time.
"""
"""
import time

def slow_function():
    total = 0
    for i in range(100000000):
        total+=i
    return total

start_time = time.time()
result = slow_function()
end_time = time.time()

print(f"Result: {result}")
print(f"Time taken: {end_time-start_time:.4f} seconds")
"""

# cProfile
"""
cProfile is a python's built-in profiling tool, offering detailed statistics like call counts, total time, and per-call time.
"""
"""
import cProfile

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    result = factorial(5)
    print(f"Result: {result}")

cProfile.run("main()")
"""
# line_profiler
"""
line_profiler (install with pip install line_profiler) profiles code line by line.
Use the @profile decorator and run with kernprof.
"""
"""
@profile
def expensive_loop():
    total = 0
    for i in range(1000):
        total += i**2
    return total
result = expensive_loop()
print(f"Result: {result}")
"""
"""
Run Commands:
kernprof -l profiling_in_python.py
python3 -m line_profiler profiling_in_python.py.lprof
"""
# memory_profiler
"""
memory_profiler (install with pip install memory_profiler) tracks memory consumption line by line.
"""
"""
from memory_profiler import profile

@profile
def memory_hog():
    a = [1] * (10 ** 6)
    b = [2] * (10 ** 6)
    return a+b

if __name__ == "__main__":
    memory_hog()
"""
"""
Run command:
python -m memory_profiler profiling_in_python.py
"""
# timieit
"""
The timeit module, built into Python, measures execution time of small code snippets across multiple runs for accuracy.
"""
import timeit

def list_comprehension():
    return [x * x for x in range(1000)]

execution_time = timeit.timeit(list_comprehension, number=1000)
print(f"Execution time for 1000 runs: {execution_time:.4f} seconds")
