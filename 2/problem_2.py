# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
    #def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# def addtwoNumbers(l1,l2):
#     myList = [l1,l2]
#     mySum = []
#     for i in myList:
#         #linkedlist reverser
#         # i = i.reverse()
#         n = int(''.join(str(j) for j in i.reverse())) 
#         mySum.append(n)
#     return sum(mySum)

# # l1 = [9,9,9,9,9,9,9]
# # l2 = [9,9,9,9]

# l1 = [2,4,3] 
# l2 = [5,6,4]
# print(addtwoNumbers(l1,l2))
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def myLinkedList(head):
#     prev = None
#     curr = head

#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next

#     return prev

# head = Node(0)
# head.next = Node(1)
# head.next.next = Node(2)
# head.next.next = Node(3)

# print(myLinkedList(head))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev  # New head

# Helper to print the list
def print_list(head):
    while head:
        print(head.value)
        head = head.next
    print("None")

# Create linked list: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original:")
print_list(head)

# Reverse it
reversed_head = reverse_linked_list(head)
print("Reversed:")
print_list(reversed_head)
