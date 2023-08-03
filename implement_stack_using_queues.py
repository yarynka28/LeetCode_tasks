import queue

class MyStack:

    def __init__(self):
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        temp_q = queue.Queue()
        while self.q.qsize() > 1:
            temp_q.put(self.q.get())
        top_element = self.q.get()
        while not temp_q.empty():
            self.q.put(temp_q.get())
        return top_element

    def top(self) -> int:
        top_element = self.pop()
        self.q.put(top_element)
        return top_element

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(5)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
