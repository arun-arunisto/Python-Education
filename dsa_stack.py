from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    #push
    def push(self, value):
        self.stack.append(value)

    #pop
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return
        self.stack.pop()

    #length
    def length(self):
        return len(self.stack)

    #peek
    def peek(self):
        return self.stack[-1]

    #print
    def display(self):
        print(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push("https://google.com/")
    s.push("https://drive.google.com/")
    s.push("https://mail.google.com/")
    s.display()
    s.pop()
    s.display()
    print(s.length())
    print(s.peek())
    s.pop()
    s.pop()
    s.pop()
