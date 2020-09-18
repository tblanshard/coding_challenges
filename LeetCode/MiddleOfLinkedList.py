# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        currentNode = head
        while currentNode.next != None:
            count += 1
            currentNode = currentNode.next
        count += 1
        count = count // 2
        node = head
        for x in range(count):
            node = node.next
        return node
        
 # ok time complexity - better than ~70%
 # poor space complexity
