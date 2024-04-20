class HashTable: 
    def __init__(self,size) -> None:
        self.data = [None] * size

    
    def _hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    
    def set(self,key,value):
        location =  self._hash(key)
        if not self.data[location]: 
            self.data[location] = []
        
        self.data[location].append([key,value])
        return self.data

    def get(self,key):
        location  = self._hash(key)
        if self.data[location]:
            for item in self.data[location]:
                if item[0] == key:
                    return item[1]
        return None
    

    # Most Worst Case
    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                for key in self.data[i]:
                    keysArray.append(key[0])
        
        return keysArray

        


new_hash_table = HashTable(3)
new_hash_table.set("name","yeasin")
new_hash_table.set("age","20")
new_hash_table.set("country","BD")
new_hash_table.set("best_friend","Raju")
new_keys = new_hash_table.keys()
print(new_keys)