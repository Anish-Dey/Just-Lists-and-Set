//https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

function removeDuplicates(head)
{
        //your code here
        let root = head
        const ls = [root.data] // using list
        
        while( root.next){
            if(ls.includes(root.next.data))
                root.next = root.next.next
            else{
                ls.push(root.next.data)
                root = root.next
            }
        }
        return head
    
    }