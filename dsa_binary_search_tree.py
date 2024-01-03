"""
sample
  left      right
        15
      /    \
    12      23
   / \     /  \
  7   14 20    27
                \
                 88
"""

#binary_search_tree
class bstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    #adding child
    def add_child(self, data):
        #checking if the data already there
        #because BST never allows duplicates
        if data == self.data:
            return

        #adding data by checking greater than or lesser
        #lesser it will move to the left
        #otherwise right
        if data < self.data:
            #checking if left have data
            if self.left:
                #recurssion method
                self.left.add_child(data)
            else:
                self.left = bstNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bstNode(data)
    

    #displaying elements in the order of traversal
    def in_order_traversal(self):
        elements = []
        
        #first visiting left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        #visiting the base node
        elements.append(self.data)

        #visiting the right tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    #displaying elements in the pre-order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements

    #displaying elements in the post-order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements

    #displaying elements in the level-order traversal
    def level_order_traversal(self):
        elements = []
        queue  = []
        queue.append(self) #appending entire node
        while len(queue) != 0:
            current_node = queue.pop(0)
            elements.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        return elements
        


    #searching inside the tree
    def search(self, value):
        #checking the self.data is the value
        if self.data == value:
            return True

        #or checking in the left tree
        if value < self.data:
            if self.left:
                #recursion
                return self.left.search(value)
            else:
                return False

        #checking on the right tree
        if value > self.data:
            if self.right:
                #recursion
                return self.right.search(value)
            else:
                return False

    #finding minimum from BST
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #finding maximum from BST
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #calculate sum
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum
    
    #delete function first apporach
    def delete_data(self, data):
        #checking value lesser than
        if data < self.data:
            if self.left:
                self.left = self.left.delete_data(data)
        #checking value greater than
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_data(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_data(min_val)

        return self

    #delete using 2nd apporach
    def delete_data_2(self, data):
        #checking value lesser than
        if data < self.data:
            if self.left:
                self.left = self.left.delete_data(data)
        #checking value greater than
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_data(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete_data(min_val)

        return self

    #getting height of the leaves left
    def get_height_left(self):
        if self.left is None:
            return 0
        hl = self.left.get_height_left()
        return hl+1

    #getting height of the leaves right
    def get_height_right(self):
        if self.right is None:
            return 0
        hr = self.right.get_height_right()
        return hr+1
        
    
#function for building tree
def build_tree(elements):
    #adding the first element as base node
    root = bstNode(elements[0])


    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__ == "__main__":
    numbers = [3, 5, 4, 7, 2, 1]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.level_order_traversal())
    #numbers = [15,12,7,14,27,20,23,88]
    #numbers_tree = build_tree(numbers)

    #numbers_hr = [3, 5, 2, 1, 4, 6, 7]
    #numbers_hr_tree = build_tree(numbers_hr)
    """print(numbers_hr_tree.in_order_traversal())
    print(numbers_hr_tree.get_height_right())
    print(numbers_hr_tree.get_height_left())
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(88))
    print(numbers_tree.search(15))
    print(numbers_tree.search(2))
    print(numbers_tree.search(155))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.calculate_sum())
    numbers_tree.delete_data(20)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete_data(14)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete_data_2(27)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.get_height_left())"""
