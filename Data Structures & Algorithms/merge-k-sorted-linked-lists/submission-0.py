import collections

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Continue merging lists until only one remains
        while len(lists) > 1:
            merged_lists = []
            # Merge adjacent pairs of lists
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # Check if there's a second list in the pair to merge
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(list1, list2))
            # The new set of lists is the result of the merges
            lists = merged_lists
        
        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # A dummy node helps simplify the code by providing a constant starting point.
        dummy_head = ListNode()
        current = dummy_head

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # At least one list is now empty. Append the non-empty one.
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return dummy_head.next