# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

def removeDuplicates(head):
        # code here
        # return head after editing list
        
    root = head
        
    ls = [root.data] # here is use list and storing the first element's data. 
    
    while root.next:
        if root.next.data in ls:
            root.next = root.next.next
        else:
            ls.append(root.next.data)
            root= root.next
        
    return head


