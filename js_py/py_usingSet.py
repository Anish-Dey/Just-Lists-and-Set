# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

def removeDuplicates(head):
        # code here
        # return head after editing list
        
    root = head
        
    hs = set() # here is use set and storing the first element's data. 
    hs.add(root.data)
    while root.next:
        if root.next.data in hs:
            root.next = root.next.next
        else:
            hs.add(root.next.data)
            root= root.next
        
    return head


