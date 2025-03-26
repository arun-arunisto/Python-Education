#subset or powerset
def backtrack_subsets(nums):
    result = []

    def backtrack(start, path):
        #adding the current subset to the result
        result.append(path[:])
        #exploring further elements
        for i in range(start, len(nums)):
            #choosing the current number
            path.append(nums[i])
            #backtracking exploring from next index
            backtrack(i+1, path)
            #undo the choice
            path.pop()
    backtrack(0, [])
    return result
"""
nums = [1, 2, 3, 4]
print("All subsets", backtrack_subsets(nums))
"""
def getting_all_substrings(a:str):
    result = []
    #converting the strings to list
    list_str = list(a)
    def substrings(start, path):
        #adding current subset to the result
        result.append(path[:])
        for i in range(start, len(list_str)):
            path.append(list_str[i])
            substrings(i+1, path)
            path.pop()
    substrings(0, [])
    return result
"""
s = "ADOBECODEBANC"
print(getting_all_substrings(s))
"""
# trying to get the subsets without the empty array
def subset_without_empty_array(arr:list):
    result = []
    def backtrack_logic(start, path):
        if path:
            result.append(path[:])
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack_logic(i+1, path)
            path.pop()
    backtrack_logic(0, [])
    return result
"""
nums = [1, 2, 2]
print(subset_without_empty_array(nums))
"""
# removing duplicates subsets
def subset_without_duplicates(arr:list):
    result = []
    def backtrack_logic(start, path):
        if path:
            result.append(path[:])
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            path.append(arr[i])
            backtrack_logic(i+1, path)
            path.pop()
    backtrack_logic(0, [])
    return result
"""
nums = [1, 2, 3]
print(subset_without_duplicates(nums))
"""
# generating all binary strings using length N
def generate_binary_str(n):
    result = []
    def backtrack_logic(current_string):
        if len(current_string) == n:
            result.append(current_string)
            return
        backtrack_logic(current_string+"0")
        backtrack_logic(current_string+"1")
    backtrack_logic('')
    return result

"""
print(generate_binary_str(2))
"""

        
