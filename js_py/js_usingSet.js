//https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

function removeDuplicates(head)
{
        //your code here
        let root = head
        const ls = new set() // here using set

        
        while( root.next){
            if(ls.has(root.next.data))
                root.next = root.next.next
            else{
                ls.add(root.next.data)
                root = root.next
            }
        }
        return head
    
    }