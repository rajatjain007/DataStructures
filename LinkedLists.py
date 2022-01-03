class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data)
        #To check if SLL is empty
        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        
        lastNode.next = newNode

    def prepend(self,data):
        newNode = Node(data)
        currentHead = self.head
        self.head = newNode
        self.head.next = currentHead

    def insert(self,data,after):
        if not after:
            print("Node to be added after doesn't exist.")
        
        newNode = Node(data)
        newNode.next = after.next
        after.next = newNode


    def printSLL(self):
        currentNode = self.head
        while currentNode:
            print(str(currentNode.data) + "->",end="")
            currentNode = currentNode.next
        print("Null",end="")
        print("")

    



sll = SingleLinkedList()
for i in range(0,10):
    sll.append(i)
print("Original SLL:")
sll.printSLL()

sll.append(10)
print("Appended SLL:")
sll.printSLL()

sll.prepend(-1)
print("Prepended SLL:")
sll.printSLL()

sll.insert(5.5,sll.head.next.next.next.next.next.next)
print("Insert after the head of SLL:")
sll.printSLL()




    
        