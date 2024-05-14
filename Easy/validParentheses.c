// Link to problem: https://leetcode.com/problems/valid-parentheses/

char pair(char s) {
    switch(s) {
        case ']': return '[';
        case '}': return '{';
        case ')': return '(';
    }
    return '\0';
}

bool isValid(char* s) {
    int length = strlen(s), top = -1;
    char stack[length];
    for (int i = 0; i < length; i++) {
        switch(s[i]) {
            case '[':
            case '{':
            case '(': stack[++top] = s[i]; break;
            case ']':
            case '}':
            case ')': {
                if (top == -1)
                    return false;
                if (pair(s[i]) != stack[top])
                    return false;
                else
                    top--;
            }
        }
    }
    return top == -1;
}