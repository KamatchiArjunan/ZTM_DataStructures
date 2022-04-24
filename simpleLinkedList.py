# Simple LinkedList Implementation
# Create a Class to define a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

# Create the LinkedList class with methods to insert nodes to the linked list and print the entire list 
class LinkedList(): 
    def printList(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        
        if head == None:
            return Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next,data)
        return head

mylist= LinkedList()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data) 
mylist.printList(head); 	  
