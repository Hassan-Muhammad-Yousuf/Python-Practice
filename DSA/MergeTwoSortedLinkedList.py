import math
import os
import random
import re
import sys
sys.setrecursionlimit(100000000)

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep=' '):
    output = []
    while node:
        output.append(str(node.data))
        node = node.next
    print(sep.join(output))

def mergeLists(head1, head2):

    if head1 == None:
        return head2
    if head2 == None:
        return head1
        
    if head1.data < head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
        return temp
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
        return temp

if __name__ == '__main__':
    # Input for the first linked list
    llist1_count = int(input("Enter number of elements in the first linked list: ").strip())  # Number of elements in the first linked list
    llist1 = SinglyLinkedList()

    print("Enter elements of the first linked list (one per line):")
    for _ in range(llist1_count):
        llist1_item = int(input().strip())  # Elements of the first linked list
        llist1.insert_node(llist1_item)

    # Input for the second linked list
    llist2_count = int(input("Enter number of elements in the second linked list: ").strip())  # Number of elements in the second linked list
    llist2 = SinglyLinkedList()

    print("Enter elements of the second linked list (one per line):")
    for _ in range(llist2_count):
        llist2_item = int(input().strip())  # Elements of the second linked list
        llist2.insert_node(llist2_item)

    # Merge the linked lists
    merged_head = mergeLists(llist1.head, llist2.head)

    # Print the merged linked list
    print("Merged Linked List:")
    print_singly_linked_list(merged_head)
