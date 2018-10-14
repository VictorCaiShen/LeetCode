class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        num_list = []
        if lists == []:
            return []
        else:
            for i in lists:
                while i:
                    num_list.append(i.val)
                    i = i.next

        num_list.sort()
        head = ListNode(0)
        first = head
        for i in num_list:
            head.next = ListNode(i)
            head = head.next

        return first.next