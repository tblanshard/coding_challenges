# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #ATTEMPT 1
        #if head.next == None:
        #    return head.val
        #else:
        #    binaryNumber = "0b"
        #    currentNode = head
        #    while currentNode.next != None:
        #        binaryNumber += str(currentNode.val)
        #        currentNode = currentNode.next
        #    binaryNumber += str(currentNode.val)
        #return int(binaryNumber,2)
        
        #ATTEMPT 2
        #binaryNumber = "0b"
        #currentNode = head
        #while currentNode.next != None:
        #    binaryNumber += str(currentNode.val)
        #    currentNode = currentNode.next
        #binaryNumber += str(currentNode.val)
        #return int(binaryNumber, 2)
    
        #ATTEMPT 3
        binaryNumber = "0b"
        while head.next != None:
            binaryNumber += str(head.val)
            head = head.next
        binaryNumber += str(head.val)
        return int(binaryNumber, 2)
