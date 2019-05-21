#Week 5, Task 1

''' This code features a linked list. I was tasked to create a function that will delete the duplicate nodes from
the linked list.'''

import unittest

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n, x):
        if n != None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next != None:
                x.next.prev = x
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x

    def display(self):
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print("List: ", ",".join(values))

    def delete_duplicates(self): # Week 5, Task 1

        '''Python doesn't really have pointers, they are more
        references to objects. They are kind of mutable memory. For
         example a temporary pointer1 gets the address of self.head, but
         it can be handled independently, without reference to head in
          particular'''

        pointer1 = self.head #head is the first node of a linked list
                            #assigns the address of head to temporary pointer
        while pointer1 != None and pointer1.next != None: #continue the loop until nodes have value
            pointer2 = pointer1 #assign another pointer, which will point to the memory address of pointer1
            while pointer2.next != None: #as long as the next node has value
                if pointer1.value == pointer2.next.value: #check if the values of both pointers match
                    pointer2.next = pointer2.next.next #results in original pointer2.next getting deleted
                else:
                    pointer2 = pointer2.next #pointer2 takes the value of the next node
            pointer1 = pointer1.next #pointer1 takes the value of the next node and continues the loop

if __name__ == '__main__':
    l = List()
    l.insert(None, Node(4))
    l.insert(l.head, Node(2))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.display()
    l.delete_duplicates()
    l.display()

