class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        New_list = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                New_list.next = l2
                l2 = l2.next
            else:
                New_list.next = l1
                l1 = l1.next
            New_list = New_list.next
        if l2 != None:
            New_list.next = l2
        elif l1 != None:
            New_list.next = l1
        return New_list.next

if __name__ == "__main__":
    s = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    print(s.mergeTwoLists(l1,l2))