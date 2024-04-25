class LinkedList:
    def __init__(self,value) -> None:
        self.head = {
            "value" : value,
            "next" : None,
            "prev" : None,
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        return f"head : {self.head} - tail : {self.tail} - length : {self.length}"
    

    def append(self, value: int) -> None:
        new_node = {
            "value" : value,
            "next" : None,
            "prev" : None
        }
        new_node["prev"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    
    def prepend(self, value : int) -> None:
        new_node = {
            "value" : value,
            "next" : None,
            "prev" : None
        }
        new_node["next"] = self.head
        self.head["prev"] = new_node
        self.head = new_node
        self.length += 1
        return self
    
    def insert(self,index: int,value : int) -> None:
        new_node = {
            "value" : value,
            "next" : None,
            "prev" : None
        }
        leader_node = self.traverser(index - 1)
        new_node["prev"] = leader_node
        new_node["next"] = leader_node["next"]
        leader_node["next"] = new_node
        new_node["next"]["prev"] = new_node
        self.length += 1
        return self

    def traverser(self,index) -> None:
        current_node = self.head
        counter = 0
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        
        return current_node
    
    def remove(self,index: int) -> None:
        leader_node = self.traverser(index - 1)
        removed_node = leader_node["next"]
        leader_node["next"] = removed_node["next"]
        removed_node["next"]["prev"] = leader_node
        self.length -= 1
        return self


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.remove(2)
my_linked_list.remove(1)

print(my_linked_list)