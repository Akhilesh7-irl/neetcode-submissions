/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map< Node* , Node* > tab;
        tab[NULL] = NULL;
        Node* cur = head;

        while(cur){
            Node* copy = new Node(cur->val);
            tab[cur] = copy;
            cur = cur->next;
        }

        cur = head;

        while (cur){
            Node* copy = tab[cur];
            copy -> next = tab[cur->next];
            copy ->random = tab[cur->random];
            cur = cur->next;
        }
        return tab[head];
    }
};
