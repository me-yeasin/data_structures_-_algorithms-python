class MyArray:
    def __init__(self) -> None:
        self.data = {}
        self.length = 0
    
    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self,index):
        delItem = self.data[index]
        self.shiftItems(index)
        return delItem

    
    def shiftItems(self,index):
        for i in range(index,self.length - 1):
            self.data[i] = self.data[i+1]
            self.length -= 1
            del self.data[self.length - 1]


    def prepend(self, item):
        for i in range(self.length, 0,-1):
            self.data[i] = self.data[i - 1]
        
        self.data[0] = item
        self.length += 1

    
    def insert(self,index,item):
        for i in range(self.length, index,-1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = item
        self.length += 1



new_array = MyArray()
new_array.push("hey")
new_array.prepend("Yeasin")
new_array.insert(1,"inseted")
print(new_array.data)
print(new_array.length)
