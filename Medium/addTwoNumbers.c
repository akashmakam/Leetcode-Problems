// Link to problem: https://leetcode.com/problems/add-two-numbers/description/


struct ListNode *createNode(int data) {
    struct ListNode *newNode = (struct ListNode *) malloc(sizeof(struct ListNode));
    if (newNode == NULL) {
        printf("\nMemory could not be dynamically allocated for the new node!\n");
        exit(1);
    }
    newNode->next = NULL;
    newNode->val = data;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *result = NULL, *current = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry) {
        int sum = carry;
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

        carry = sum / 10;
        sum %= 10;

        struct ListNode* newNode = createNode(sum);
        if (result == NULL) {
            result = newNode;
            current = result;
        } else {
            current->next = newNode;
            current = current->next;
        }
    }

    return result;
}