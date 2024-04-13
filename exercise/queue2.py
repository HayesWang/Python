class Queue:
    def __init__(self,maxSize=100):
        self.maxSize=maxSize
        self.items=[0]*maxSize
        self.front=0
        self.rear=0
    def enqueue(self,item):
        if not self.is_leak:
            self.rear=(self.rear+1)%self.maxSize
            self.items[self.rear]=item
        else:
            print("Leak")
    def dequeue(self):
        if not self.is_empty:
            self.front=(self.front+1)%self.maxSize
            return self.items[self.front]
    def is_leak(self):
        if (self.rear+1)%self.maxSize==self.front:
            return True
        else:
            return False
    def is_empty(self):
        return self.items==[]