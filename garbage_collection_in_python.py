# Garbage Collection
"""
In Python, garbage collection (GC) is the process of automatically reclaiming
memory occupied by objects that are no longer in use.
Python manages memory for you, so you generally don’t have to manually
free memory like in C or C++.
"""
# How python keeps track of objects
"""
Python mainly uses reference counting to
track whether an object is still needed:
"""
# Example
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))
# this will return 2 because:
# sys.getrefcount() always includes the
# temporary reference from the function argument

b = a
print(sys.getrefcount(a)) # this will return 3 "a" and "b" and sys.getrefcount()

del b
print(sys.getrefcount(a)) # this will return 2 because b got deleted

"""
- Every object has a reference count.

- When it drops to 0, Python can immediately free the memory.

- Problem: Reference counting alone can't handle circular references.
"""
# Circular References
"""
A circular reference is when objects refer to each other, creating a cycle.
"""
a = {}
b = {}

a['b'] = b
b['a'] = a

print(sys.getrefcount(a)) # this will return 3
del a
del b
"""
After deleting also both dictionaries are still in memory,
because they reference each other.
Even though a and b are deleted, each dictionary still has a reference
to the other. Python’s reference counting alone cannot delete them.
"""

# the garbage collector module
"""
Python uses the gc module to handle circular references.
It periodically runs to detect cycles and frees memory.
"""
"""
First we will verify using gc that the objects are still in memory
"""
# Verifying objects are still in memory
import gc

# enabling the garbage collection
gc.enable()

# all objects tracked by the garbage collection
all_obj = gc.get_objects() # it will return all the objects tracked
# verifying 'a' and 'b' dict() are there
print(any(isinstance(i, dict) and 'b' in i and 'a' in i['b'] for i in all_obj))
"""
if it's True, that means the dictionaries are still in the memory.
"""
"""
You can also see what it collects:
"""
print(gc.set_debug(gc.DEBUG_UNCOLLECTABLE))
# Manually trigger garbage collection
collected = gc.collect() # force GC to run
print(f"Garbage collector collected objects: {collected}")
"""
- gc.collect() searches for unreachable objects (like cycles) and
frees their memory.

- Now the memory used by a and b is cleaned.
"""
# Garbage Collection uses generational collection
"""
- Gen 0: new objects, collected frequently.

- Gen 1: survived one collection, collected less often.

- Gen 2: long-lived objects, collected rarely.

- gc.collect() without arguments collects all generations by default.
"""
# collecting specific generation:
gc.collect(0) # generation 0
gc.collect(1) # generation 1
gc.collect(2) # generation 2

# Summary
"""
1. Reference counting cannot clean circular references.

2. The garbage collector detects unreachable cycles and frees them.

3. Use gc.collect() to manually trigger cleanup if needed (rarely required).

4. Always avoid keeping unnecessary references to objects in cycles,
especially with large structures.
"""
