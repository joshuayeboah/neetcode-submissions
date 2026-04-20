# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


















        # l1 = list1
        # l2 = list2
        # smaller = None

        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         smaller = l1
        #     else:
        #         smaller = l2

            
        #     if l1.val <= l2.val:
        #         smaller.next = l1
        #     smaller.next = l2
        # return smaller
        