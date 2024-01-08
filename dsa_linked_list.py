class Node: #creating a class node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList: #LinkedList class
    def __init__(self):
        self.head = None

    #functions like adding element deleting element
    def insert_at_end(self, data):
        # adding node[contains data] to head if head is None
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return

        #adding data back2back
        current_data = self.head
        while current_data.next:
            current_data = current_data.next
        current_data.next = Node(data)

    #adding multiple data into linkedlist
    def insert_many_at_once(self, data, empty=False):
        #if empty change into True it will remove all existing elements
        if empty:
            self.head = None
        for d in data:
            self.insert_at_end(d)

    #inserting elements at beginning of the nodes
    def insert_at_start(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    #getting length of the list
    def get_length(self):
        #if data none it will return 0
        if self.head is None:
            print(0)
            return

        #total data
        total = 0
        data_iter = self.head
        while data_iter:
            total+=1
            data_iter = data_iter.next
        return total #it will print the total data

    #removing the last element from the list
    def remove_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        #removing last element
        count = 0
        data_iter = self.head
        while data_iter:
            count+=1
            if count == self.get_length()-1:
                data_iter.next = data_iter.next.next
                break
            data_iter = data_iter.next

    #removing the first element from the list
    def remove_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    #inserting using index
    def insert_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("Index not in range")
        #if index is 0
        if index == 0:
            new_node = Node(data, self.head)
            self.head = new_node

        count = 0
        data_iter = self.head
        while data_iter:
            count+=1
            if count == index:
                new_node = Node(data, data_iter.next)
                data_iter.next = new_node
                break
            data_iter = data_iter.next

    #removing data using index
    def remove_index(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index not in range")
        #removing if position is 0
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        data_iter = self.head
        while data_iter:
            if count == index-1:
                data_iter.next = data_iter.next.next
                break
            count+=1
            data_iter = data_iter.next

    #removing data using data
    def remove_data(self, data):
        data_iter = self.head
        previous = None
        while data_iter:
            if data_iter.data == data:
                if previous:
                    previous.next = data_iter.next
                else:
                    self.head = data_iter.next
                return
            previous = data_iter
            data_iter = data_iter.next
    
    #removing duplicates
    def remove_duplicates(self):
        current = self.head
        duplicates = {}
        while current:
            if current.data not in duplicates:
                duplicates[current.data] = 1
                current = current.next
            else:
                next_data = current.next
                self.remove_data(current.data)
                current = next_data
    
    #displaying the data
    def display_data(self):
        if self.head is None:
            print("List is Empty")
            return

        #if self.head containing data
        data_iter = self.head
        while data_iter:
            print(data_iter.data, end=" ")
            data_iter = data_iter.next

if __name__ == "__main__":
    li = LinkedList()
    li.insert_at_end(25)
    li.insert_at_end(45)
    li.insert_at_end(75)
    li.insert_many_at_once([12, 34, 56, 78])
    li.insert_at_start("Arunisto")
    print("Length:",li.get_length())
    li.remove_at_end()
    li.remove_at_end()
    li.remove_at_start()
    li.insert_index(2, 80)
    li.insert_index(0, "arun")
    li.insert_index(7, "Hello")
    li.remove_index(0)
    li.remove_index(2)
    li.remove_index(5)
    li.remove_data(25)
    li.remove_data(75)
    li.display_data()
            
        
