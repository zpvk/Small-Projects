class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self,val):
        self.val = val

    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next

# linklis class

class LinkedList(object):
    def __init__ (self, head=None):
        self.head = head
        self.count = 0 

    def get_count(self):
        return self.count
    
    def insert(self, data):
        new_node =  Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self,val):
        item = self.head
        while (item !=None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self,idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            tempIdex = 0
            node = self.head
            while tempIdex < idx-1:
                node = node.get_next()
                tempIdex +=1
            node.set_next(node.get_next1().get_next())
            self.count -=1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

#create a link list and insert some items

itemlist = LinkedList()
itemlist.insert(34)
itemlist.insert(65)
itemlist.insert(45)
itemlist.insert(90)

itemlist.dump_list()

print("Finding item: ", itemlist.find(90))



    


