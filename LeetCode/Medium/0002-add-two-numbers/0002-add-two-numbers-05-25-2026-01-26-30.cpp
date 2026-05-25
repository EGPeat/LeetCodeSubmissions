/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy_head = new ListNode();
        int carry = 0;
        ListNode* current_node = dummy_head;
        while (l1 or l2 or carry){
            int digit1 = 0, digit2 = 0;
            if(l1 and l1->val > 0){digit1 = l1->val;}//no idea if this works
            if(l2 and l2->val > 0){digit2 = l2->val;}
            cout << digit1 <<" " << digit2 <<" " << carry<<endl;
            int total_sum = digit1 + digit2 + carry;
            int digit_value = total_sum % 10;
            carry = total_sum / 10;
            cout << digit1 <<" " << digit2 <<" " << carry<<endl;
            cout << "###############################"<<endl;
            current_node->next = new ListNode(digit_value);
            current_node = current_node->next;
            if (l1){l1 = l1->next;}
            else{l1 = NULL;}
            if (l2){l2 = l2->next;}
            else{l2 = NULL;}

        }
        return dummy_head->next;
    }
};