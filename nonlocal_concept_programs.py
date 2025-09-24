# Practise Problems for nonlocal
"""
Q1. Counter Function

Write a function make_counter() that returns an increment() function.
Every time you call increment(),it should increase the counter by
1 and return the current count.
"""

def make_counter():
    x = 0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter

c = make_counter()
print(c())
print(c())
print(c())
print(c())

"""
Q2. Toggle Switch

Write a function make_toggle() that returns a function switch().
Every time you call switch(), it should toggle between "ON" and "OFF".
"""

def toggle_switch():
    state = False
    def switch():
        nonlocal state
        state = not state
        return "ON" if state else "OFF"
    return switch

switch = toggle_switch()
print(switch())
print(switch())
print(switch())

"""
Q3. Running Total

Write a function make_adder(start=0) that returns a function add(x).
Each time you call add(x), it should add x to the running total and return it.
"""

def running_total(start):
    def adder(x):
        nonlocal start
        start = start+x
        return start
    return adder

runner = running_total(10)
print(runner(5))
print(runner(3))
print(runner(8))

"""
Q4. Limited Calls

Write a function limit_calls(func, max_calls) that takes another function
and returns a wrapped version. The wrapped function should only allow
max_calls executions — after that, it should print "No more calls allowed".
"""

def limit_calls(func, tries):
    max_tries = 0
    def max_try():
        nonlocal max_tries
        max_tries += 1
        return func() if max_tries <= tries else print("No more calls allowed")
    return max_try

def hello():
    print("Hello!")

limited_calls = limit_calls(hello, 2)
limited_calls()
limited_calls()
limited_calls()

"""
Q5. Function Call History (Decorator Style)

Create a decorator @track_calls that keeps a history of all arguments
passed to the function. Use nonlocal to store the history.
"""

def track_calls(func):
    local_storage = []
    def wrapper(n):
        nonlocal local_storage
        local_storage.append(n)
        return f"Call history: {local_storage}"
    return wrapper

@track_calls
def square(n):
    return n*n

print(square(2))
print(square(3))
print(square(4))
    

        
