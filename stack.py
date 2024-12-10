class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
        # return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
def reverse_string(str):
    reversed_str = ""
    s = Stack()
    
    # i = 0
    # while(i < len(str)):
    #     s.push(str[i])
    #     i += 1
    for char in str:
        s.push(char)
    
    while not s.is_empty():
        reversed_str += s.pop()
        
    return reversed_str

    
    
if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push('hi')
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())
    print(reverse_string('Hello'))