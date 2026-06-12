class MinStack:

    def __init__(self):
        self.arr=[]
        self.min=float('inf')
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min=min(self.min,val)
        

    def pop(self) -> None:
        if len(self.arr)==0:
            return -1
        removeEle= self.arr.pop()
        if(self.min==removeEle):
            self.min=float('inf')
            for ele in self.arr:
                self.min=min(self.min,ele)
        return removeEle

        

    def top(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        if len(self.arr)==0:
            return -1 
        return self.min
        
