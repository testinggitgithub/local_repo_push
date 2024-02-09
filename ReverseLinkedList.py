# Python3 program to reverse a Linked List 
# in groups of given size 
  
# Node class 
class Node(object): 
    __slots__ = 'data', 'next'
  
    # Constructor to initialize the node object 
    def __init__(self, data = None, next = None): 
        self.data = data 
        self.next = next
  
    def __repr__(self): 
        return repr(self.data) 
  
class LinkedList(object): 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Utility function to print nodes  
    # of LinkedList 
    def __repr__(self): 
        nodes = [] 
        curr = self.head 
        while curr: 
            nodes.append(repr(curr)) 
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'
  
    # Function to insert a new node at 
    # the beginning 
    def prepend(self, data): 
        self.head = Node(data = data, 
                         next = self.head) 
  
    # Reverses the linked list in groups of size k 
    # and returns the pointer to the new head node. 
    def reverse(self, k = 1): 
        if self.head is None: 
            return
  
        curr = self.head 
        prev = None
        new_stack = [] 
        while curr is not None: 
            val = 0
              
            # Terminate the loop whichever comes first 
            # either current == None or value >= k 
            while curr is not None and val < k: 
                new_stack.append(curr.data) 
                curr = curr.next
                val += 1
  
            # Now pop the elements of stack one by one 
            while new_stack: 
                  
                # If final list has not been started yet. 
                if prev is None: 
                    prev = Node(new_stack.pop()) 
                    self.head = prev 
                else: 
                    prev.next = Node(new_stack.pop()) 
                    prev = prev.next
                      
        # Next of last element will point to None. 
        prev.next = None
        return self.head 
  
# Driver Code 
llist = LinkedList()  
llist.prepend(9) 
llist.prepend(8) 
llist.prepend(7) 
llist.prepend(6) 
llist.prepend(5) 
llist.prepend(4) 
llist.prepend(3) 
llist.prepend(2) 
llist.prepend(1) 
  
print("Given linked list") 
print(llist) 
llist.head = llist.reverse(3) 
  
print("Reversed Linked list") 
print(llist) 
  
 