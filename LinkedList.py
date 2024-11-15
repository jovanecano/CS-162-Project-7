#Author: Jovane Cano
#GitHub Username: jovanecano
#Date: 11/13/2024
#Description: Linked list which contains recursive implementations of the add and remove methods from our explorations

"""Creating the Node class and initializing with data and a pointer to the next node"""
class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

"""Creating the linked list class containing various recursive methods"""
class LinkedList:
    def __init__(self):
        self._head = None # initializing the ll with a private head node at None

    def get_head(self):
    # get method that returns the first node
        return self._head

    def rec_add(self, a_node, data):
        # this recursive method whcih adds the data to the end of the list
        # if its at the end it creates a new node
        if a_node.next is None:
            a_node.next = Node(data)
        else:
            self.rec_add(a_node.next, data) # keeps traversing until end is reached

    def add(self, data):
        #the add method will add a node with given data to the end of list and will create first node if list is empty
        if self._head is None:
            self._head = Node(data)
        else:
            self.rec_add(self._head, data)

    def rec_remove(self, a_node, data):
        # rec_remove, a recursive method will remove a node with particular data
        if a_node is None or a_node.next is None:
            return #does nothing is end is reached or node is None
        if a_node.next.data == data:
            a_node.next = a_node.next.next
        else:
            self.rec_remove(a_node.next, data)

    def remove(self, data):
        #remove method will remove the first node with the given data from list
        if self._head is None:
            return
        #if head contains the data, it removes it by the next node as the head
        if self._head.data == data:
            self._head = self._head.next
        else:
            self.rec_remove(self._head, data)

    def rec_contains(self, a_node, data):
        #recursive method that will check if a node with the specific data exists, returns true if so, false otherwise
        if a_node is None:
            return False
        if a_node.data == data:
            return True
        return self.rec_contains(self._head, data)

    def contains(self, data):
        #checks if the list contains a node with the specific data
        return self.rec_contains(self._head, data)

    def rec_insert(self, a_node, data, pos):
        #recursive helper method that inserts a node with data at a specified position
        if pos == 1:
            new_node = Node(data)
            new_node.next = a_node.next
            a_node.next = new_node
        elif a_node.next is not None:
            self.rec_insert(a_node.next, data, pos - 1) #will continue to the next node and decremnt the pos

    def insert(self, data, pos):
    #the insert method will inesrt a node with the given data at a specified position
        if pos == 0:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
        else:
            self.rec_insert(self._head, data, pos)

    def rec_reverse(self, a_node, prev=None):
        #recursive helper method that will reverse the linked list by changing next pointers
        if a_node is None:
            self._head = prev
        else:
            next_node = a_node.next #stores node in temp var
            a_node.next = prev #changes pointer to prev
            self.rec_reverse(next_node, a_node)

    def reverse(self):
        # reverses the list
        self.rec_reverse(self._head)

    def rec_to_plain_list(self, a_node):
        #recursive helper method that converts the list into python strd list
        if a_node is None:
            return []
        return [a_node.data] + self.rec_to_plain_list(a_node.next)

    def to_plain_list(self):
        return self.rec_to_plain_list(self._head)

    def rec_display(self, a_node):
        #recursive helper function that prints data from nodes within list
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        #prints the data from list
        self.rec_display(self._head)
        print()