class LinkedList:
    def __init__(self,value):
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head # pointing memory location of head
        self.length = 1

    # a util function to print the linked list
    def __str__(self) -> str:
        return f"head : {self.head} - tail {self.tail} - length : {self.length}"
    

    def append (self,value):
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail["next"] = new_node # getting "next" from head memory location
        self.tail = new_node # now pointing tail to the new memory location which is "next"
        self.length += 1
        return self

    
    def prepend (self,value):
        new_node = {
            "value" : value,
            "next" : None,
        }

        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        return self
    

    def print_list(self):
        result_arr = []
        current_node = self.head
        while current_node != None:
                result_arr.append(current_node["value"])
                current_node = current_node["next"]
        print(result_arr)


    def insert(self,index,value):
        new_node = {
              "value" : value,
              "next" : None
        }
        
        if(index == 0):
             self.prepend(new_node)
             self.length += 1
             return self

        leader_node = self.traverseToIndex(index - 1)
        temp_node = leader_node["next"]
        leader_node["next"] = new_node
        new_node["next"] = temp_node
        self.length += 1
        return self

    def traverseToIndex(self,index):
        counter = 0
        current_node = self.head
        while counter != index:
             current_node = current_node["next"]
             counter += 1
        return current_node
    
    def delete(self,index):
         leader_node = self.traverseToIndex(index - 1)
         deleted_node = leader_node["next"]
         holding_node = deleted_node["next"]
         leader_node["next"] = holding_node
         self.length -= 1
         return deleted_node
    
    def findByIndex(self,index):
         finded_node = self.traverseToIndex(index)
         return finded_node
    
    def reverse_list(self) -> None:
        first_node = self.head
        self.tail = self.head
        second_node = self.head["next"]
        while second_node != None:
             temp_node = second_node["next"]
             second_node["next"] = first_node
             first_node = second_node
             second_node = temp_node
        
        self.head["next"] = None
        self.head = first_node
        return self

# myLinkList = LinkedList(1)
# myLinkList.append(2)
# myLinkList.append(3)
# myLinkList.append(4)
# myLinkList.append(5)
# myLinkList.reverse_list()
# print(myLinkList)