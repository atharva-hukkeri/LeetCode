class MyStack:
    def __init__(self):
        self.queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        while len(self.queue) > 0:
            self.helper_queue.append(self.queue.popleft())
            
        self.queue.append(x)
        
        while len(self.helper_queue) > 0:
            self.queue.append(self.helper_queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()    
        
    def top(self) -> int:
        return self.queue[0]  

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()