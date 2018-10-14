# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        k1 = self.length(head)//k
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        for i in range(k1):
            first = pre.next
            last = pre.next
            while k-1:
                if last.next != None:
                    last = last.next
                    k -= 1
                else:
                    break
            later = last.next
            if last != None and last.next != None:
                first.next = later
                last.next = first
                pre.next = last
                pre = last

        return new_head.next

    def length(self, head):
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count
