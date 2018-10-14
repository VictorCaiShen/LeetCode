class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        while pre.next != None and pre.next.next != None:
            node1 = pre.next
            node2 = pre.next.next
            node3 = pre.next.next.next

            pre.next = node2
            node1.next = node3
            node2.next = node1

            pre = node1

        return new_head.next
